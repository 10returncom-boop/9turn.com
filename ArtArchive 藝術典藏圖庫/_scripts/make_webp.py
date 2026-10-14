#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_webp.py — ArtArchive 生成 WebP 預覽與縮圖
============================================
職責：
  從 01_OriginalRaw 原始母檔批次產生：
    - 02_WebPreview：WebP 預覽圖（網站用，寬邊上限 1600、品質 80）
    - 03_Thumbnail：小縮圖（寬邊上限 320、品質 75）
  檔名沿用原檔名（含 art_id），確保與 art_archive.csv 一一對應。
  僅處理標準檔名 ARTxxxxx-分類-作者-標題-年代.ext 的圖檔。

依賴：Pillow（python -m pip install -r requirements.txt）

用法：
    python make_webp.py                          # 用預設 ArtArchive 根目錄
    python make_webp.py --archive-root ".." --preview-width 1600 --thumb-width 320
    python make_webp.py --dry-run                # 只列出將產生的檔案
"""
import argparse
import os
import re
import sys

from PIL import Image, ImageOps

ORIGINAL_DIR = "01_OriginalRaw"
WEBP_DIR = "02_WebPreview"
THUMB_DIR = "03_Thumbnail"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp"}
FILENAME_RE = re.compile(
    r"^(ART\d+)-(.+)\.(?P<ext>[^.]+)$", re.IGNORECASE)


def resolve_category_dir(category: str) -> str:
    """把分類對應到子資料夾（A_油畫 / B_雕塑 / C_水墨）。"""
    table = {
        "油畫": "A_油畫", "雕塑": "B_雕塑", "水墨": "C_水墨",
        "A_油畫": "A_油畫", "B_雕塑": "B_雕塑", "C_水墨": "C_水墨",
    }
    return table.get(category, "A_油畫" if category == "油畫" else category)


def open_auto_orient(path: str) -> Image.Image:
    """開圖並依 EXIF 自動旋正。"""
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGB")
    return img


def save_webp(img: Image.Image, out_path: str, quality: int):
    img.save(out_path, "WEBP", quality=quality, method=6)


def main():
    ap = argparse.ArgumentParser(description="生成 WebP 預覽與縮圖")
    ap.add_argument("--archive-root", default=None,
                    help="ArtArchive 根目錄（預設：本腳本上層資料夾）")
    ap.add_argument("--preview-width", type=int, default=1600, help="預覽圖寬邊上限（預設 1600）")
    ap.add_argument("--preview-quality", type=int, default=80, help="預覽品質（預設 80）")
    ap.add_argument("--thumb-width", type=int, default=320, help="縮圖寬邊上限（預設 320）")
    ap.add_argument("--thumb-quality", type=int, default=75, help="縮圖品質（預設 75）")
    ap.add_argument("--dry-run", action="store_true", help="只列出計畫")
    ap.add_argument("--source-dir", default=None,
                    help="指定原始檔資料夾（預設 01_OriginalRaw 全部分類）")
    args = ap.parse_args()

    if args.archive_root is None:
        args.archive_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = os.path.abspath(args.archive_root)

    if args.source_dir:
        search_root = os.path.abspath(args.source_dir)
    else:
        search_root = os.path.join(root, ORIGINAL_DIR)
    if not os.path.isdir(search_root):
        sys.exit(f"錯誤：找不到原始檔資料夾 {search_root}")

    originals = []
    for dirpath, _d, files in os.walk(search_root):
        for fn in sorted(files):
            if os.path.splitext(fn)[1].lower() in IMAGE_EXTS:
                originals.append(os.path.join(dirpath, fn))
    if not originals:
        sys.exit("錯誤：來源資料夾內沒有任何圖檔")

    made = skipped = 0
    for src in originals:
        base = os.path.basename(src)
        m = FILENAME_RE.match(base)
        if not m:
            skipped += 1
            print(f"略過（非標準檔名）：{src}")
            continue
        stem = m.group(1) + "-" + m.group(2)          # ART00001-油畫-莫內-睡蓮-1916
        category = m.group(2).split("-")[0]           # 取分類段
        out_dir = os.path.join(root, WEBP_DIR, resolve_category_dir(category))
        thumb_dir = os.path.join(root, THUMB_DIR, resolve_category_dir(category))
        os.makedirs(out_dir, exist_ok=True)
        os.makedirs(thumb_dir, exist_ok=True)

        webp_out = os.path.join(out_dir, stem + ".webp")
        thumb_out = os.path.join(thumb_dir, stem + ".webp")

        if args.dry_run:
            print(f"  將產生：{os.path.relpath(webp_out, root)} / {os.path.relpath(thumb_out, root)}")
            made += 1
            continue

        try:
            img = open_auto_orient(src)
            ratio = args.preview_width / max(img.size)
            if ratio < 1:
                img_preview = img.resize((round(img.width * ratio), round(img.height * ratio)), Image.LANCZOS)
            else:
                img_preview = img
            save_webp(img_preview, webp_out, args.preview_quality)

            tr = args.thumb_width / max(img.size)
            img_thumb = img.resize((round(img.width * tr), round(img.height * tr)), Image.LANCZOS) if tr < 1 else img
            save_webp(img_thumb, thumb_out, args.thumb_quality)
            made += 1
        except Exception as e:
            print(f"失敗：{src} → {e}")
            continue

    print(f"完成：生成 {made} 組，略過 {skipped} 個非標準檔名。")


if __name__ == "__main__":
    main()
