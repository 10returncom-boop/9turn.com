#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_art_data.py — 從 art_archive.csv 重建頁面資料 art_data.js
================================================================
用途：正式圖庫建好後，把 CSV 內容轉成 index.html 用的 window.ART_DATA。
  1. 讀取 art_archive.csv
  2. 每筆作品取：縮圖(thumb)、預覽(preview)、原始(original)路徑或 Drive 連結
     - 優先使用 gdrive_*_url（上傳後）
     - 沒有則用本機 WebP 路徑（換算成相對 index.html 的相對路徑）
  3. 寫入 ArtArchive 根目錄的 art_data.js

用法：
    python _scripts\\build_art_data.py
    python _scripts\\build_art_data.py --csv "..\\art_archive.csv" --out "..\\art_data.js"
"""
import argparse
import csv
import json
import os
import sys


def rel(root: str, path: str) -> str:
    """絕對路徑 → 相對於頁面(root)的相對路徑（使用正斜線）。"""
    try:
        return os.path.relpath(path, root).replace("\\", "/")
    except Exception:
        return path


def main():
    ap = argparse.ArgumentParser(description="從 CSV 重建 art_data.js")
    ap.add_argument("--csv", default=None, help="art_archive.csv 路徑")
    ap.add_argument("--out", default=None, help="art_data.js 輸出路徑")
    args = ap.parse_args()

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # ArtArchive 根
    csv_path = os.path.abspath(args.csv or os.path.join(base, "art_archive.csv"))
    out_path = os.path.abspath(args.out or os.path.join(base, "art_data.js"))

    if not os.path.exists(csv_path):
        sys.exit(f"錯誤：找不到 {csv_path}")

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    entries = []
    for r in rows:
        art_id = (r.get("art_id") or "").strip()
        if not art_id:
            continue
        wp = (r.get("webp_path") or "").strip()
        tp = (r.get("thumb_path") or "").strip()
        op = (r.get("original_path") or "").strip()
        gwebp = (r.get("gdrive_webp_url") or "").strip()
        gthumb = (r.get("gdrive_thumb_url") or "").strip()
        gorig = (r.get("gdrive_original_url") or "").strip()

        # 至少要有可顯示的預覽/縮圖來源，否則不放入頁面
        preview = gwebp or (rel(base, wp) if wp and os.path.exists(wp) else "")
        thumb = gthumb or (rel(base, tp) if tp and os.path.exists(tp) else preview)
        original = gorig or (rel(base, op) if op and os.path.exists(op) else "")
        if not preview and not thumb:
            continue

        entries.append({
            "art_id": art_id,
            "category": (r.get("category") or "").strip(),
            "artist": (r.get("artist") or "").strip(),
            "title": (r.get("title") or "").strip(),
            "year": (r.get("year") or "").strip(),
            "thumb": thumb,
            "preview": preview,
            "original": original,
            "gdrive_original_url": gorig,
            "gdrive_webp_url": gwebp,
            "gdrive_thumb_url": gthumb,
        })

    body = ("/* ArtArchive 頁面資料（由 _scripts/build_art_data.py 從 art_archive.csv 自動重建）*/\n"
            "window.ART_DATA = " + json.dumps(entries, ensure_ascii=False, indent=2) + ";\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"完成：寫入 {len(entries)} 筆 → {out_path}")


if __name__ == "__main__":
    main()
