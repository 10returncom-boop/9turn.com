# -*- coding: utf-8 -*-
"""
9TURN 九回錦｜deep_data 深度模組批次檢核（_deep_check.py）
檢核 9 個資產模組：
  1) 匯入成功且 ARTICLES 長度 == 22
  2) slug 全唯一
  3) 每篇 7 欄位齊全（slug/h1/title/lede/desc/kw/body）
  4) body 字數（去標籤後中文字元+標點）約 800–1200
  5) 每篇 ≥4 個 h2；至少 1 張 webp img（含 alt）；含「你該怎麼用」
用法：python _deep_check.py
"""
import os, re, importlib, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

MODS = ["art", "estate", "antique", "jewelry", "wine_tea", "timber", "watch", "instrument", "coin_stamp"]
FIELDS = ["slug", "h1", "title", "lede", "desc", "kw", "body"]

def visible_len(body):
    s = re.sub(r"<[^>]+>", "", body)
    s = re.sub(r"\s+", "", s)
    return len(s)

def main():
    total_issues = 0
    for mod in MODS:
        issues = []
        try:
            m = importlib.import_module(f"deep_data.{mod}")
        except Exception as e:
            print(f"[{mod}] 匯入失敗：{e}")
            total_issues += 1
            continue
        arts = getattr(m, "ARTICLES", [])
        if len(arts) != 22:
            issues.append(f"篇數 {len(arts)}（預期 22）")
        slugs = [a.get("slug", "") for a in arts]
        if len(slugs) != len(set(slugs)):
            dup = [s for s in slugs if slugs.count(s) > 1]
            issues.append(f"slug 重複：{set(dup)}")
        for i, a in enumerate(arts, 1):
            miss = [f for f in FIELDS if not a.get(f)]
            if miss:
                issues.append(f"第{i:02d}篇缺欄位：{miss}")
            body = a.get("body", "")
            n = visible_len(body)
            if n < 750 or n > 1300:
                issues.append(f"第{i:02d}篇字數 {n}（目標 800–1200）")
            h2 = len(re.findall(r"<h2", body))
            if h2 < 4:
                issues.append(f"第{i:02d}篇 h2 數 {h2}（需 ≥4）")
            imgs = re.findall(r'<img[^>]+src="([^"]+\.webp)"[^>]*>', body)
            if not imgs:
                issues.append(f"第{i:02d}篇無 webp 圖")
            elif not all('alt="' in re.search(r"<img[^>]+>", body).group(0) for _ in imgs):
                issues.append(f"第{i:02d}篇 img 缺 alt")
            if "你該怎麼用" not in body:
                issues.append(f"第{i:02d}篇缺「你該怎麼用」")
        if issues:
            total_issues += len(issues)
            print(f"[{mod}] {len(issues)} 個問題：")
            for it in issues[:12]:
                print("  -", it)
        else:
            print(f"[{mod}] OK：22 篇、slug 唯一、欄位齊全、字數/h2/圖/「你該怎麼用」全過")
    print(f"\n總問題數：{total_issues}")

if __name__ == "__main__":
    main()
