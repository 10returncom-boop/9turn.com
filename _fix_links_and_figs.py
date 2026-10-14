# -*- coding: utf-8 -*-
"""一次性修補：
1) 把所有 href/src 裡的 '..//' 修正為 '../'（解決網址列出現 '///'）。
2) 移除所有內頁文章開頭的 <figure class="asset-fig">...</figure> 配圖（含後續換行）。
保留首頁卡片圖、pillar 圖、box-img、rel-card 等視覺。
"""
import io, os, re, sys

ROOT = r"D:\_WWW_325_public\9turn.com九回錦3"
# 跳過截圖快取與獨立圖庫子站（結構不同）
SKIP_DIRS = {"_shots", "ArtArchive 藝術典藏圖庫", "node_modules", ".git"}

fig_re = re.compile(r'<figure class="asset-fig">.*?</figure>\s*', re.S)

def fix(path):
    s = io.open(path, encoding="utf-8").read()
    orig = s
    # 1) 修雙斜杠
    s = s.replace("..//", "../")
    # 2) 移除 asset-fig 配圖
    s, n_fig = fig_re.subn("", s)
    if s != orig:
        io.open(path, "w", encoding="utf-8", newline="").write(s)
    return s != orig, n_fig

changed = 0
fig_removed = 0
files_seen = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        if not fn.lower().endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        files_seen += 1
        ch, nf = fix(p)
        if ch:
            changed += 1
            fig_removed += nf

print(f"掃描 HTML：{files_seen} 個")
print(f"修改檔案：{changed} 個")
print(f"移除 asset-fig 配圖：{fig_removed} 個")

# 驗證：全站不應再出現 '..//' 或 'asset-fig'
bad_slash = 0
bad_fig = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        if not fn.lower().endswith(".html"):
            continue
        p = os.path.join(dirpath, fn)
        s = io.open(p, encoding="utf-8").read()
        if "..//" in s:
            bad_slash += 1
        if "asset-fig" in s:
            bad_fig += 1
print(f"驗證：仍含 '..//' 的檔案 = {bad_slash}；仍含 'asset-fig' 的檔案 = {bad_fig}")
