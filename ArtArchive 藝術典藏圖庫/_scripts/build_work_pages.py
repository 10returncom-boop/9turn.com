#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_work_pages.py — 產生每件作品的獨立 HTML 頁（SSG）
======================================================
依 art_archive.csv 為每一件作品產生 ART<id>.html（如 ART00001.html），
本機可直接雙擊開啟預覽，符合靜態網站「每件作品一個獨立頁」的架構。

用法：
    python _scripts\\build_work_pages.py
"""
import argparse
import csv
import html
import os
import sys

PAGE_CSS = """
:root{--bg:#121417;--surface:#181b1f;--panel:#20242a;--text:#ece6da;--muted:#98917f;--faint:#6c6759;
--hairline:rgba(236,230,218,.10);--hairline-strong:rgba(236,230,218,.18);--gold:#c9a86a;
--serif:'Noto Serif SC','Songti TC','SimSun',serif;--sans:'Noto Sans SC','PingFang TC','Microsoft JhengHei',sans-serif;}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--bg);color:var(--text);font-family:var(--sans);font-weight:300;line-height:1.6;-webkit-font-smoothing:antialiased;}
a{color:inherit;text-decoration:none;}
.top{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;
 max-width:1120px;margin:0 auto;padding:18px 22px;border-bottom:1px solid var(--hairline);}
.back{color:var(--gold);font-size:.86rem;border:1px solid var(--hairline);padding:8px 16px;border-radius:999px;transition:border-color .2s;}
.back:hover{border-color:var(--gold);}
.brand{font-family:var(--serif);font-size:1.02rem;letter-spacing:.02em;}
.wrap{max-width:1120px;margin:0 auto;padding:40px 22px 20px;display:flex;gap:40px;align-items:flex-start;flex-wrap:wrap;}
.artwork{flex:1 1 420px;min-width:0;}
.artwork img{width:100%;border-radius:8px;box-shadow:0 30px 70px rgba(0,0,0,.55);}
.meta{flex:0 0 300px;padding-top:8px;}
.kicker{font-size:.72rem;color:var(--gold);letter-spacing:.22em;text-transform:uppercase;}
h1{font-family:var(--serif);font-weight:600;font-size:2rem;margin-top:10px;line-height:1.3;}
.rows{margin-top:22px;}
.row{padding:13px 0;border-top:1px solid var(--hairline);font-size:.9rem;}
.row dt{color:var(--faint);font-size:.72rem;letter-spacing:.12em;margin-bottom:2px;}
.row dd{color:var(--text);}
.notes{color:var(--muted);font-size:.84rem;margin-top:18px;padding:12px 14px;border:1px solid var(--hairline);border-radius:6px;}
.nav{max-width:1120px;margin:22px auto 0;padding:0 22px;display:flex;gap:12px;}
.nav a{flex:1;border:1px solid var(--hairline);border-radius:8px;padding:16px 18px;text-align:center;transition:border-color .2s;background:var(--surface);}
.nav a:hover{border-color:var(--gold);}
.nav .d{display:block;font-size:.68rem;color:var(--faint);letter-spacing:.1em;margin-bottom:4px;}
.nav .t{font-family:var(--serif);font-size:1rem;}
.nav .disabled{opacity:.35;pointer-events:none;}
footer{max-width:1120px;margin:40px auto 0;padding:20px 22px 46px;border-top:1px solid var(--hairline);
 color:var(--faint);font-size:.78rem;text-align:center;}
@media(max-width:720px){.wrap{gap:24px;padding-top:24px;}.meta{flex:1 1 100%;}.nav a{padding:13px 10px;}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;}}
"""


def esc(s):
    return html.escape(s or "", quote=True)


def build_page(work, prev_work, next_work):
    title = work["title"]
    artist = work["artist"]
    year = work["year"]
    art_id = work["art_id"]
    category = work["category"]
    preview = work["preview"] or work["thumb"] or ""
    gorig = work.get("gdrive_original_url", "")

    def nav_block(w, label):
        if not w:
            return f'<a class="disabled" aria-disabled="true"><span class="d">{label}</span><span class="t">—</span></a>'
        return (f'<a href="{esc(w["art_id"])}.html"><span class="d">{label}</span>'
                f'<span class="t">{esc(w["title"])}</span></a>')

    original_note = ""
    if gorig:
        original_note = '<div class="row"><dt>原始母檔</dt><dd>僅典藏帳號可存取的私密連結（不對外）</dd></div>'

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} · ArtArchive 藝術典藏</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' rx='4' fill='%23121417'/%3E%3Crect x='7' y='7' width='10' height='10' rx='1.5' stroke='%23c9a86a' stroke-width='1.6' fill='none'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://miaoda.feishu.cn">
<link rel="stylesheet" href="https://miaoda.feishu.cn/fonts/css2?family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@300;400;500;600&display=swap">
<style>{PAGE_CSS}</style>
</head>
<body>
<header class="top">
  <div class="brand">九回錦 · 藝術典藏</div>
  <a class="back" href="index.html">← 回畫廊</a>
</header>

<main class="wrap">
  <figure class="artwork">
    <img src="{esc(preview)}" alt="{esc(title)}">
  </figure>
  <div class="meta">
    <div class="kicker">{esc(category)}</div>
    <h1>{esc(title)}</h1>
    <div class="rows">
      <div class="row"><dt>編號</dt><dd>{esc(art_id)}</dd></div>
      <div class="row"><dt>作者</dt><dd>{esc(artist) or '—'}</dd></div>
      <div class="row"><dt>年代</dt><dd>{esc(year) or '—'}</dd></div>
      <div class="row"><dt>分類</dt><dd>{esc(category)}</dd></div>
      {original_note}
    </div>
    <div class="notes">此頁為靜態單頁（SSG 產生），圖片取自本機 WebP 預覽；正式上線後可由 Google Drive 預覽圖連結載入。</div>
  </div>
</main>

<nav class="nav">
  {nav_block(prev_work, '上一件')}
  {nav_block(next_work, '下一件')}
</nav>

<footer>ArtArchive · 藝術典藏圖庫 — 靜態單頁檢視</footer>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="產生每作品獨立 HTML 頁")
    ap.add_argument("--csv", default=None)
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.abspath(args.csv or os.path.join(base, "art_archive.csv"))
    out_dir = os.path.abspath(args.out_dir or base)
    os.makedirs(out_dir, exist_ok=True)

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    works = []
    for r in rows:
        art_id = (r.get("art_id") or "").strip()
        if not art_id:
            continue
        preview = (r.get("gdrive_webp_url") or "").strip()
        if not preview:
            wp = (r.get("webp_path") or "").strip()
            preview = os.path.relpath(wp, out_dir).replace("\\", "/") if wp else ""
        works.append({
            "art_id": art_id,
            "category": (r.get("category") or "").strip(),
            "artist": (r.get("artist") or "").strip(),
            "title": (r.get("title") or "").strip(),
            "year": (r.get("year") or "").strip(),
            "preview": preview,
            "gdrive_original_url": (r.get("gdrive_original_url") or "").strip(),
        })
    works.sort(key=lambda w: w["art_id"])

    made = 0
    for i, w in enumerate(works):
        prev_w = works[i - 1] if i > 0 else None
        next_w = works[i + 1] if i < len(works) - 1 else None
        page = build_page(w, prev_w, next_w)
        with open(os.path.join(out_dir, w["art_id"] + ".html"), "w", encoding="utf-8") as fo:
            fo.write(page)
        made += 1
    print(f"完成：產生 {made} 個獨立頁 → {out_dir}")


if __name__ == "__main__":
    main()
