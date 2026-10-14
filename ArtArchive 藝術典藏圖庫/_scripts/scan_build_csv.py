#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan_build_csv.py — ArtArchive 掃描與建 CSV 腳本
=================================================
職責（僅處理本機檔案，不碰 Google Drive）：
  1. 掃描來源資料夾內所有圖檔（jpg/jpeg/png/webp/tif/tiff）
  2. 解析檔名 → art_id / category / artist / title / year
  3. 若檔名未含 art_id，自動依序指派 ART00001...
  4. 計算每張原始檔的 MD5 雜湊
  5. 比對 02_WebPreview、03_Thumbnail 是否已有對應預覽/縮圖
  6. 寫入 / 更新 art_archive.csv（UTF-8 帶 BOM）

檔名規範（與 CSV art_id 一一對應）：
    ART00001-油畫-莫內-睡蓮-1916.webp
    格式：ART<5位數>-<分類>-<作者>-<標題>-<年代>.<副檔名>
    其中「標題」允許含連字號（採用貪婪匹配，取最後一段 - 年份 前的全部）。

用法範例：
    python scan_build_csv.py --source "D:\\_WWW_325\\篆刻金石聽故事" --csv "..\\art_archive.csv"
    python scan_build_csv.py --source "D:\\a,D:\\b" --dry-run          # 只列計畫不寫入
"""
import argparse
import csv
import hashlib
import os
import re
import sys

# 支援的圖檔副檔名
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp"}

# 標準檔名：ART00001-油畫-莫內-睡蓮-1916.webp（標題貪婪匹配）
FILENAME_RE = re.compile(
    r"^ART(?P<art_id>\d+)-(?P<category>[^-]+)-(?P<artist>[^-]+)-"
    r"(?P<title>.+)-(?P<year>\d{4})\.(?P<ext>[^.]+)$",
    re.IGNORECASE,
)

CSV_FIELDS = [
    "art_id", "category", "artist", "title", "year",
    "filename", "original_path", "webp_path", "thumb_path",
    "md5_original", "md5_webp", "md5_thumb",
    "gdrive_original_url", "gdrive_webp_url", "gdrive_thumb_url",
    "status", "notes",
]


def md5_file(path: str, chunk: int = 1024 * 1024) -> str:
    """計算檔案 MD5（大檔分批讀取）。"""
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def find_images(source: str):
    """走訪資料夾，回傳所有圖檔絕對路徑（依檔名排序）。"""
    hits = []
    if os.path.isfile(source):
        hits.append(source)
    else:
        for dirpath, _dirs, files in os.walk(source):
            for fn in files:
                if os.path.splitext(fn)[1].lower() in IMAGE_EXTS:
                    hits.append(os.path.join(dirpath, fn))
    return sorted(hits)


def parse_filename(filename: str, fallback_category: str):
    """解析單一檔名。回傳 dict 或 None（無法解析時回傳 None，由呼叫方兜底）。"""
    m = FILENAME_RE.match(filename)
    if not m:
        return None
    cat = m.group("category")
    if not cat:
        cat = fallback_category
    return {
        "art_id": "ART" + m.group("art_id").zfill(5),
        "category": cat,
        "artist": m.group("artist").strip(),
        "title": m.group("title").strip(),
        "year": m.group("year"),
    }


def normalize_category(name: str) -> str:
    """把資料夾名對應到分類：A_油畫→油畫、B_雕塑→雕塑、C_水墨→水墨。"""
    name = name.strip()
    table = {
        "a_油畫": "油畫", "油畫": "油畫",
        "b_雕塑": "雕塑", "雕塑": "雕塑",
        "c_水墨": "水墨", "水墨": "水墨",
    }
    return table.get(name, name)


def read_existing(csv_path: str) -> dict:
    """讀取既有 CSV，回傳 {art_id: row}。"""
    out = {}
    if not os.path.exists(csv_path):
        return out
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("art_id"):
                out[row["art_id"]] = row
    return out


def write_csv(csv_path: str, rows: list):
    """以 UTF-8 帶 BOM 寫回 CSV，確保 Excel 正確顯示中文。"""
    os.makedirs(os.path.dirname(csv_path) or ".", exist_ok=True)
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            # 保留既有欄位，並確保所有欄位鍵都存在
            clean = {k: r.get(k, "") if r.get(k) is not None else "" for k in CSV_FIELDS}
            writer.writerow(clean)


def locate_derivatives(art_id: str, archive_root: str, category: str):
    """在 02_WebPreview / 03_Thumbnail 找對應檔案。回傳 (webp_path, thumb_path)。"""
    def find_in(top: str):
        for cat_dir in (category, "A_油畫", "B_雕塑", "C_水墨"):
            base = os.path.join(archive_root, top, cat_dir)
            for fn in os.listdir(base) if os.path.isdir(base) else []:
                if fn.upper().startswith(art_id + "-"):
                    return os.path.join(base, fn)
        return ""
    return find_in("02_WebPreview"), find_in("03_Thumbnail")


def main():
    ap = argparse.ArgumentParser(description="ArtArchive 掃描並建立 art_archive.csv")
    ap.add_argument("--source", required=True,
                    help="來源圖檔資料夾（多個以半形逗號分隔，或直接給單一檔案）")
    ap.add_argument("--csv", default=None,
                    help="CSV 路徑（預設：本機 ArtArchive 根目錄下 art_archive.csv）")
    ap.add_argument("--archive-root", default=None,
                    help="ArtArchive 根目錄（預設為 --csv 的上層資料夾）")
    ap.add_argument("--dry-run", action="store_true",
                    help="只列出將寫入的記錄，不實際寫檔")
    ap.add_argument("--no-merge", action="store_true",
                    help="不與既有 CSV 合併（從頭重建）")
    args = ap.parse_args()

    if args.csv is None:
        args.csv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "art_archive.csv")
    archive_root = args.archive_root or os.path.dirname(args.csv)
    csv_path = os.path.abspath(args.csv)

    sources = [s.strip() for s in args.source.split(",") if s.strip()]
    if not sources:
        sys.exit("錯誤：--source 不可為空")

    existing = {} if args.no_merge else read_existing(csv_path)
    next_seq = 1
    if existing:
        nums = [int(k[3:]) for k in existing if k.upper().startswith("ART") and k[3:].isdigit()]
        next_seq = (max(nums) + 1) if nums else 1

    rows = []
    seen = set(existing.keys())
    for src in sources:
        files = find_images(src)
        if not files:
            print(f"警告：來源無任何圖檔 → {src}")
            continue
        for path in files:
            base = os.path.basename(path)
            parent = os.path.basename(os.path.dirname(path))
            fallback_cat = normalize_category(parent)
            parsed = parse_filename(base, fallback_cat)

            if parsed and parsed["art_id"] in existing:
                row = dict(existing[parsed["art_id"]])          # 已存在：保留原記錄
                row["original_path"] = path
                row["md5_original"] = md5_file(path)
            else:
                art_id = parsed["art_id"] if parsed else f"ART{next_seq:05d}"
                if art_id in seen:
                    # 同一批內重複 id：改成新序號
                    while f"ART{next_seq:05d}" in seen:
                        next_seq += 1
                    art_id = f"ART{next_seq:05d}"
                next_seq += 1
                row = {
                    "art_id": art_id,
                    "category": parsed["category"] if parsed else fallback_cat,
                    "artist": parsed["artist"] if parsed else "",
                    "title": parsed["title"] if parsed else os.path.splitext(base)[0],
                    "year": parsed["year"] if parsed else "",
                    "filename": base,
                    "original_path": path,
                    "webp_path": "",
                    "thumb_path": "",
                    "md5_original": md5_file(path),
                    "md5_webp": "",
                    "md5_thumb": "",
                    "gdrive_original_url": "",
                    "gdrive_webp_url": "",
                    "gdrive_thumb_url": "",
                    "status": "local",
                    "notes": "",
                }
            # 比對預覽/縮圖（若已生成）
            wp, th = locate_derivatives(row["art_id"], archive_root, row["category"])
            if wp and os.path.exists(wp):
                row["webp_path"] = wp
                row["md5_webp"] = md5_file(wp)
            if th and os.path.exists(th):
                row["thumb_path"] = th
                row["md5_thumb"] = md5_file(th)
            seen.add(row["art_id"])
            rows.append(row)

    rows.sort(key=lambda r: r["art_id"])
    if args.dry_run:
        print(f"[DRY-RUN] 將寫入 {len(rows)} 筆至 {csv_path}")
        for r in rows[:20]:
            print("  ", r["art_id"], "|", r["category"], "|", r["artist"], "|",
                  r["title"], "|", r["year"], "|", r["md5_original"][:10])
        return
    write_csv(csv_path, rows)
    print(f"完成：寫入 {len(rows)} 筆 → {csv_path}")


if __name__ == "__main__":
    main()
