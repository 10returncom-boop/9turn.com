#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
upload_share_links.py — ArtArchive 上傳 Google Drive 並回填分享連結
================================================================
職責：
  1. 讀取 art_archive.csv
  2. 以 Google Drive API（服務帳號）上傳：
     - 01_OriginalRaw/<分類>：原始母檔 → 完全私密，不設任何分享權限
     - 02_WebPreview/<分類>：WebP 預覽 → 「知道連結的人可檢視」(anyone, reader)
     - 03_Thumbnail/<分類>：縮圖 → 同樣「知道連結的人可檢視」
  3. 抓取預覽/縮圖的 webViewLink，回填 CSV 的 gdrive_webp_url / gdrive_thumb_url
  4. 具冪等性：同檔名已上傳過就跳過，可安全重跑

前置準備（請先完成，見 README「前置設定」）：
  - 建立 Google Cloud 專案，啟用 Google Drive API
  - 建立服務帳號，下載 JSON 憑證，記下其 email
  - 在專用典藏 Google 帳號的 Drive，把「ArtArchive」資料夾共用給該服務帳號 email（權限：編輯者）
  - 設定環境變數 SERVICE_ACCOUNT_FILE（指向 JSON 憑證路徑）

用法：
    python upload_share_links.py --csv "..\\art_archive.csv" --root-folder-id <ArtArchive資料夾ID>
    python upload_share_links.py --dry-run
"""
import argparse
import os
import sys

try:
    from dotenv import load_dotenv
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
except ImportError:
    sys.exit("缺少依賴：請先 python -m pip install -r requirements.txt")

# ===== 資料夾結構（與本機骨架一致）=====
ORIGINAL_DIR = "01_OriginalRaw"
WEBP_DIR = "02_WebPreview"
THUMB_DIR = "03_Thumbnail"

CATEGORY_DIRS = {
    "油畫": "A_油畫",
    "雕塑": "B_雕塑",
    "水墨": "C_水墨",
}

CSV_FIELDS = [
    "art_id", "category", "artist", "title", "year",
    "filename", "original_path", "webp_path", "thumb_path",
    "md5_original", "md5_webp", "md5_thumb",
    "gdrive_original_url", "gdrive_webp_url", "gdrive_thumb_url",
    "status", "notes",
]

SCOPES = ["https://www.googleapis.com/auth/drive"]


def get_service():
    svc_file = os.environ.get("SERVICE_ACCOUNT_FILE")
    if not svc_file or not os.path.exists(svc_file):
        sys.exit("找不到 SERVICE_ACCOUNT_FILE（服務帳號 JSON 憑證）。請在 .env 設定。")
    creds = service_account.Credentials.from_service_account_file(svc_file, scopes=SCOPES)
    return build("drive", "v3", credentials=creds)


def _folder_id_by_name(svc, parent_id, name):
    """依名稱在 parent 下找資料夾，找不到回傳 None。"""
    q = f"name='{name.replace(chr(39), chr(92)+chr(39))}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents and trashed=false"
    res = svc.files().list(q=q, fields="files(id)").execute()
    files = res.get("files", [])
    return files[0]["id"] if files else None


def _create_folder(svc, name, parent_id):
    meta = {"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [parent_id]}
    f = svc.files().create(body=meta, fields="id").execute()
    return f["id"]


def ensure_folder_tree(svc, root_id):
    """確保 Drive 資料夾樹存在，回傳 { '01_OriginalRaw': {cat: id}, ... }"""
    tree = {}
    for top in (ORIGINAL_DIR, WEBP_DIR, THUMB_DIR):
        tid = _folder_id_by_name(svc, root_id, top) or _create_folder(svc, top, root_id)
        tree[top] = {"_id": tid}
        for cat, sub in CATEGORY_DIRS.items():
            sid = _folder_id_by_name(svc, tid, sub) or _create_folder(svc, sub, tid)
            tree[top][cat] = sid
    return tree


def find_file_by_name(svc, folder_id, name):
    q = (f"name='{name.replace(chr(39), chr(92)+chr(39))}' and "
         f"'{folder_id}' in parents and trashed=false")
    res = svc.files().list(q=q, fields="files(id,webViewLink)").execute()
    return res.get("files", [None])[0]


def upload_file(svc, folder_id, local_path, filename):
    """上傳單檔，回傳 file dict（含 id、webViewLink）。"""
    media = MediaFileUpload(local_path, resumable=True)
    meta = {"name": filename, "parents": [folder_id]}
    f = svc.files().create(body=meta, media_body=media, fields="id,webViewLink").execute()
    return f


def set_anyone_link_permission(svc, file_id):
    """設權限：知道連結的人可檢視（anyone / reader），不會被搜尋索引。"""
    svc.permissions().create(
        fileId=file_id, body={"type": "anyone", "role": "reader"}
    ).execute()


def main():
    ap = argparse.ArgumentParser(description="上傳 ArtArchive 至 Google Drive 並回填連結")
    ap.add_argument("--csv", default=None, help="art_archive.csv 路徑")
    ap.add_argument("--root-folder-id", required=True,
                    help="專用典藏 Drive 中 ArtArchive 資料夾的 ID")
    ap.add_argument("--dry-run", action="store_true", help="只列出上傳計畫")
    ap.add_argument("--skip-original", action="store_true",
                    help="略過原始母檔上傳（只上傳預覽/縮圖）")
    args = ap.parse_args()

    load_dotenv()
    if args.csv is None:
        args.csv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "art_archive.csv")
    csv_path = os.path.abspath(args.csv)

    import csv as _csv
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(_csv.DictReader(f))

    svc = get_service() if not args.dry_run else None
    tree = None if args.dry_run else ensure_folder_tree(svc, args.root_folder_id)

    orig_count = prev_count = thumb_count = 0
    for row in rows:
        art_id = row.get("art_id", "")
        cat = row.get("category", "")
        sub = CATEGORY_DIRS.get(cat, "A_油畫")

        # --- 原始母檔（私密，不設分享）---
        op = row.get("original_path", "").strip()
        if op and os.path.exists(op) and not args.skip_original:
            fname = os.path.basename(op)
            if args.dry_run:
                print(f"[DRY] 上傳(私密) {fname} → {ORIGINAL_DIR}/{sub}")
                orig_count += 1
            else:
                fid = tree[ORIGINAL_DIR][cat if cat in CATEGORY_DIRS else "油畫"]
                if find_file_by_name(svc, fid, fname):
                    print(f"略過(已存在) {fname}")
                else:
                    upload_file(svc, fid, op, fname)
                    orig_count += 1

        # --- 預覽圖（anyone/reader）---
        wp = row.get("webp_path", "").strip()
        if wp and os.path.exists(wp):
            fname = os.path.basename(wp)
            if args.dry_run:
                print(f"[DRY] 上傳(連結檢視) {fname} → {WEBP_DIR}/{sub}")
                prev_count += 1
            else:
                fid = tree[WEBP_DIR][cat if cat in CATEGORY_DIRS else "油畫"]
                found = find_file_by_name(svc, fid, fname)
                if found:
                    row["gdrive_webp_url"] = found.get("webViewLink", row.get("gdrive_webp_url", ""))
                else:
                    f = upload_file(svc, fid, wp, fname)
                    set_anyone_link_permission(svc, f["id"])
                    link = svc.files().get(fileId=f["id"], fields="webViewLink").execute().get("webViewLink", "")
                    row["gdrive_webp_url"] = link
                    prev_count += 1

        # --- 縮圖（anyone/reader）---
        tp = row.get("thumb_path", "").strip()
        if tp and os.path.exists(tp):
            fname = os.path.basename(tp)
            if args.dry_run:
                print(f"[DRY] 上傳(連結檢視) {fname} → {THUMB_DIR}/{sub}")
                thumb_count += 1
            else:
                fid = tree[THUMB_DIR][cat if cat in CATEGORY_DIRS else "油畫"]
                found = find_file_by_name(svc, fid, fname)
                if found:
                    row["gdrive_thumb_url"] = found.get("webViewLink", row.get("gdrive_thumb_url", ""))
                else:
                    f = upload_file(svc, fid, tp, fname)
                    set_anyone_link_permission(svc, f["id"])
                    link = svc.files().get(fileId=f["id"], fields="webViewLink").execute().get("webViewLink", "")
                    row["gdrive_thumb_url"] = link
                    thumb_count += 1

        row["status"] = "uploaded" if (not args.dry_run and (row.get("gdrive_webp_url") or row.get("gdrive_thumb_url"))) else row.get("status", "local")

    if not args.dry_run:
        import csv as _c2
        os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)
        with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = _c2.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
            writer.writeheader()
            for r in rows:
                clean = {k: (r.get(k, "") if r.get(k) is not None else "") for k in CSV_FIELDS}
                writer.writerow(clean)
        print(f"完成：原始 {orig_count}、預覽 {prev_count}、縮圖 {thumb_count}，已回填 {csv_path}")
    else:
        print(f"[DRY-RUN] 將上傳：原始 {orig_count}、預覽 {prev_count}、縮圖 {thumb_count}")


if __name__ == "__main__":
    main()
