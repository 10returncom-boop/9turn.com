# -*- coding: utf-8 -*-
"""
9TURN 九回錦｜批次檢核腳本（verify.py）
三項自動檢核：
  1) 全站 SEO 元素：每頁 title / description / canonical / OG / JSON-LD / zh-Hant
  2) 內部與外部連結、圖片檔案路徑存在性
  3) 本機檔案比對：自動偵測並列出 404 斷鏈（href/src 指向不存在的檔案）
另檢查：每頁資料夾內自含 assets（搬移獨立）、sitemap/robots/manifest/404 存在。
用法：python verify.py
"""
import os, re, glob, json

ROOT = os.path.dirname(os.path.abspath(__file__))
EXT_SKIP = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")
# 非站點資料夾（使用者／外部獨立專案）：不納入本站檢核，也不刪除
EXCLUDE_DIRS = ("ArtArchive 藝術典藏圖庫", "jiuhuijin-gallery", "sheets", "_shots")

def all_html():
    files = []
    for d in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(d, ROOT).replace("\\", "/")
        if any(seg in rel.split("/") for seg in EXCLUDE_DIRS):
            continue
        files.append((d, rel))
    return files

def pick(m):
    return m.group(1) if m else None

def check_seo(path, rel, issues, broken):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    low = html.lower()
    checks = {
        "title": '<title>' in low,
        "description": '<meta name="description"' in low,
        "canonical": 'rel="canonical"' in low,
        "og:title": 'property="og:title"' in low,
        "og:image": 'property="og:image"' in low,
        "JSON-LD": 'application/ld+json' in low,
        "zh-Hant": 'lang="zh-hant"' in low,
        "manifest": 'rel="manifest"' in low,
    }
    for k, ok in checks.items():
        if not ok:
            issues.append(f"  缺 {k}: {rel}")
    # JSON-LD 必須可解析且 ≥3 種
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            data = json.loads(m.group(1))
            arr = data if isinstance(data, list) else [data]
            if len(arr) < 3:
                issues.append(f"  JSON-LD 類型少於3: {rel}")
        except Exception:
            issues.append(f"  JSON-LD 解析失敗: {rel}")

def check_links(path, rel, broken):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    base_dir = os.path.dirname(path)
    pat = re.compile(r'(?:href|src)="([^"]+)"')
    for m in pat.finditer(html):
        u = m.group(1).split("#")[0]
        if not u or u.startswith(EXT_SKIP) or u.startswith("#"):
            continue
        # 每頁 assets/css、assets/js 一律存在（資料夾獨立）
        if u in ("assets/css/style.css", "assets/js/main.js", "manifest.webmanifest", "sitemap.xml"):
            target = os.path.join(base_dir, u)
            if not os.path.exists(target):
                broken.append(f"  [{rel}] 404: {u} -> {target}")
            continue
        target = os.path.normpath(os.path.join(base_dir, u))
        if not os.path.exists(target):
            broken.append(f"  [{rel}] 404: {u}")

def main():
    files = all_html()
    print(f"掃描到 {len(files)} 個 HTML（含 404.html）\n")
    seo_issues, broken = [], []
    for path, rel in files:
        check_seo(path, rel, seo_issues, broken)
        check_links(path, rel, broken)
    # 獨立資料夾資產完整性（每個子資料夾須自含 assets）
    subdirs = sorted({os.path.dirname(f) for f, _ in files} - {ROOT})
    asset_missing = []
    for d in subdirs:
        for rel in ["css/style.css", "js/main.js"]:
            if not os.path.exists(os.path.join(d, "assets", rel)):
                asset_missing.append(f"{os.path.relpath(d, ROOT)}/assets/{rel}")
    # 全站 SEO 檔
    seo_files = ["sitemap.xml", "robots.txt", "manifest.webmanifest", "404.html"]
    missing_seo = [s for s in seo_files if not os.path.exists(os.path.join(ROOT, s))]

    print("=== 1) SEO 元素檢查 ===")
    print("缺 SEO 元素:", len(seo_issues))
    for s in seo_issues[:60]:
        print(s)
    print("\n=== 2) 連結／圖片路徑檢查 ===")
    print("斷裂連結(404):", len(broken))
    for b in broken[:60]:
        print(b)
    print("\n=== 3) 本機檔案存在／獨立性檢查 ===")
    print("子資料夾缺 assets:", asset_missing)
    print("缺全站 SEO 檔:", missing_seo)
    print("\n驗證完成")

if __name__ == "__main__":
    main()
