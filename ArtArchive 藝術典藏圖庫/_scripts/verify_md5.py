#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_md5.py — ArtArchive MD5 完整性校驗
======================================
職責：
  1. 讀取 art_archive.csv
  2. 對每一筆重新計算 original / webp / thumb 的 MD5
  3. 與 CSV 中紀錄值比對，揪出被替換、損毀、或檔案遺失的圖檔
  4. 結尾印出總結，任一不符即以非零狀態碼結束（便於 CI 判失敗）

用法：
    python verify_md5.py
    python verify_md5.py --csv "..\\art_archive.csv" --fail-fast
    python verify_md5.py --missing-only        # 只列出遺失檔案
"""
import argparse
import csv
import hashlib
import os
import sys


def md5_file(path: str, chunk: int = 1024 * 1024) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description="ArtArchive MD5 校驗")
    ap.add_argument("--csv", default=None, help="art_archive.csv 路徑")
    ap.add_argument("--fail-fast", action="store_true", help="發現第一個錯誤即停止")
    ap.add_argument("--missing-only", action="store_true", help="只列出檔案遺失項目")
    args = ap.parse_args()

    if args.csv is None:
        args.csv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "art_archive.csv")
    csv_path = os.path.abspath(args.csv)

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    check_map = [("original_path", "md5_original"), ("webp_path", "md5_webp"), ("thumb_path", "md5_thumb")]
    total = missing = mismatch = ok = 0
    problems = []

    for row in rows:
        art_id = row.get("art_id", "?")
        for path_field, md5_field in check_map:
            p = (row.get(path_field) or "").strip()
            if not p:
                continue
            total += 1
            if not os.path.exists(p):
                missing += 1
                problems.append(f"[遺失] {art_id}  {path_field}: {p}")
                if args.missing_only:
                    print(f"[遺失] {art_id}  {path_field}: {p}")
                if args.fail_fast:
                    sys.exit(f"FAIL：檔案遺失 {art_id}")
                continue
            expect = (row.get(md5_field) or "").strip().lower()
            actual = md5_file(p)
            if not expect:
                mismatch += 1
                problems.append(f"[無基準] {art_id}  {path_field}: 無 MD5 基準值")
                continue
            if actual != expect:
                mismatch += 1
                problems.append(f"[不符] {art_id}  {path_field}:\n    基準 {expect}\n    現算 {actual}")
                if args.fail_fast:
                    sys.exit(f"FAIL：MD5 不符 {art_id} {path_field}")
            else:
                ok += 1

    print(f"校驗結果：總計 {total} 個檔案，OK {ok}，遺失 {missing}，不符/無基準 {mismatch}。")
    if not args.missing_only:
        for line in problems:
            print(line)
    if missing or mismatch:
        sys.exit(f"FAIL：{missing} 遺失、{mismatch} 不符/無基準。")
    print("PASS：全部檔案 MD5 一致。")


if __name__ == "__main__":
    main()
