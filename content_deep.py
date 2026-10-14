# -*- coding: utf-8 -*-
"""
9Turn 九回錦｜深度內容（九大資產 × 22 篇 = 198 篇）框架
- 每個資產一個子目錄：asset/<key>/
  · index.html        子類總覽（22 篇文章卡片導覽）
  · 01-….html … 22 篇深層知識文章
- 頁面的 crumb / sidebar / prev-next / SEO meta 全部由本框架自動組，
  資料模組 deep_data/<key>.py 只負責內容（ARTICLES list）。
"""
import importlib

# 九大資產註冊表：key → (主頁標題, 主頁檔名, 深度專區名稱)
ASSETS = {
    "art":       {"name": "典藏藝術品",        "main": "art.html",        "deep_name": "藝術品深度專區"},
    "estate":    {"name": "典藏宅邸／稀有地產", "main": "estate.html",     "deep_name": "稀有地產深度專區"},
    "antique":   {"name": "古董文玩",          "main": "antique.html",    "deep_name": "古董文玩深度專區"},
    "jewelry":   {"name": "珍稀珠寶",          "main": "jewelry.html",    "deep_name": "珍稀珠寶深度專區"},
    "wine-tea":  {"name": "經典酒茶",          "main": "wine-tea.html",   "deep_name": "經典酒茶深度專區"},
    "timber":    {"name": "頂級原木",          "main": "timber.html",     "deep_name": "頂級原木深度專區"},
    "watch":     {"name": "經典名錶",          "main": "watch.html",       "deep_name": "經典名錶深度專區"},
    "instrument":{"name": "經典樂器",          "main": "instrument.html", "deep_name": "經典樂器深度專區"},
    "coin-stamp":{"name": "珍稀錢幣與珍郵",    "main": "coin-stamp.html",  "deep_name": "錢幣珍郵深度專區"},
}

PAGES = {}
DATE = "2026-10-14"


def _load_articles(key):
    """載入 deep_data.<key>.ARTICLES；檔名連字號對應底線模組名（wine-tea → wine_tea）"""
    mod_name = key.replace("-", "_")
    try:
        mod = importlib.import_module(f"deep_data.{mod_name}")
        return getattr(mod, "ARTICLES", [])
    except Exception as e:
        print(f"[deep] 警告：deep_data.{mod_name} 載入失敗：{e}")
        return []


def _sidebar(asset, articles, current_slug, img_key="art"):
    """文章側欄：總覽連結 + 22 篇導覽（box 頂部配資產圖）"""
    top = (
        '<div class="box"><h4>' + asset["name"] + '</h4><ul>'
        f'<li><a href="../../asset/{asset["main"]}">← 回到{asset["name"]}主頁</a></li>'
        '<li><a href="index.html">深度專區總覽</a></li>'
        '</ul></div>'
    )
    lis = []
    for i, a in enumerate(articles, 1):
        cls = "active" if a["slug"] == current_slug else ""
        lis.append(
            f'<li><a class="{cls}" href="{a["slug"]}.html">'
            f'<span class="mini-num">{i:02d}</span>{a["h1"]}</a></li>'
        )
    return top + ('<div class="box"><h4>22 篇文章導覽</h4>'
                  '<ul style="max-height:62vh;overflow:auto">' + "".join(lis) + "</ul></div>")


def _build_index(key, asset, articles):
    """資產深度專區總覽頁（asset/<key>/index.html）"""
    cards = []
    for i, a in enumerate(articles, 1):
        cards.append(
            f'<a class="rel-card" href="{a["slug"]}.html">'
            f'<span class="rc-tag">第 {i:02d} 篇</span>'
            f'<span class="rc-title">{a["h1"]}</span></a>'
        )
    body = (
        f'<h2>1. 這個專區在讀什麼？</h2>'
        f'<p>{asset["name"]}主頁先給你全景，這個深度專區把它拆成 <strong>22 篇專題文章</strong>，'
        f'從入門觀念、鑑定查驗、市場週期、保存倉儲一路講到家族傳承。每篇 800–1200 字，痛點開頭、大白話講透。</p>'
        f'<h2>2. 22 篇文章導覽</h2>'
        f'<div class="rel-grid" style="grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">'
        + "".join(cards) + '</div>'
        f'<h2>3. 看完之後</h2>'
        f'<div class="callout"><div class="ico">錦</div><div>'
        f'把 22 篇讀完，你對{asset["name"]}的認識會從「聽過名牌」升級到「能自己判斷真假與價值」。'
        f'<a href="../../asset/{asset["main"]}">← 回到{asset["name"]}主頁</a></div></div>'
    )
    return {
        "out_dir": f"asset/{key}", "file": "index.html",
        "title": f'{asset["name"]}深度專區｜22 篇知識文章 — 9Turn 九回錦',
        "desc": f'9Turn 九回錦{asset["name"]}深度專區：22 篇專業知識文章，從鑑定、市場、保存到傳承，'
                f'帶你把{asset["name"]}這門學問一次讀透。',
        "kw": f'9Turn,九回錦,{asset["name"]},深度專區,典藏知識,硬資產',
        "section": "九大資產深度專區",
        "deep_name": asset["deep_name"],
        "crumb": [("首頁", "../../index.html"), ("九大資產", "../../asset/index.html"),
                  (asset["name"], "../../asset/" + asset["main"]),
                  (asset["deep_name"], "index.html")],
        "h1": f'{asset["name"]}深度專區：22 篇文章讀透這門學問',
        "lede": f'全景看過了？這 22 篇專題把{asset["name"]}從頭到尾拆開講——鑑定、市場、保存、傳承，一篇都不少。',
        "layout": "2col",
        "sidebar_html": _sidebar(asset, articles, "", {"coin-stamp": "coin"}.get(key, key)),
        "prev": (f"{asset['name']}主頁", "../../asset/" + asset["main"]),
        "next": (articles[0]["h1"] if articles else "", articles[0]["slug"] + ".html") if articles else None,
        "body": body,
        "date": DATE,
    }


def _build_article(key, asset, articles, idx, art):
    """單篇深度文章頁"""
    slug = art["slug"]
    h1 = art["h1"]
    prev = (f"第 {idx:02d} 篇", f"{articles[idx-1]['slug']}.html") if idx > 0 else ("深度專區總覽", "index.html")
    if idx + 1 < len(articles):
        nxt = (articles[idx + 1]["h1"], articles[idx + 1]["slug"] + ".html")
    else:
        nxt = (f"{asset['name']}主頁", "../../asset/" + asset["main"])
    return {
        "out_dir": f"asset/{key}", "file": slug + ".html",
        "title": f'{art["title"]}｜9Turn 九回錦',
        "desc": art.get("desc", f'9Turn 九回錦{asset["name"]}深度知識：{h1}'),
        "kw": art.get("kw", f'9Turn,九回錦,{asset["name"]},' + h1),
        "section": "九大資產深度專區",
        "deep_name": asset["deep_name"],
        "crumb": [("首頁", "../../index.html"), ("九大資產", "../../asset/index.html"),
                  (asset["name"], "../../asset/" + asset["main"]),
                  (asset["deep_name"], "index.html"),
                  (h1, slug + ".html")],
        "h1": h1,
        "lede": art["lede"],
        "layout": "2col",
        "sidebar_html": _sidebar(asset, articles, slug, {"coin-stamp": "coin"}.get(key, key)),
        "prev": prev,
        "next": nxt,
        "body": art["body"],
        "date": DATE,
    }


# ---------- 組裝 ----------
for key, asset in ASSETS.items():
    arts = _load_articles(key)
    if len(arts) != 22:
        print(f"[deep] {key}: 載入 {len(arts)} 篇（預期 22 篇）")
    if not arts:
        continue
    seen = set()
    for a in arts:
        if a["slug"] in seen:
            raise ValueError(f"[deep] {key} 重複 slug: {a['slug']}")
        seen.add(a["slug"])
    PAGES[f"deep-{key}-index"] = _build_index(key, asset, arts)
    for i, a in enumerate(arts):
        PAGES[f"deep-{key}-{a['slug']}"] = _build_article(key, asset, arts, i, a)

print(f"[deep] content_deep 組裝完成：{len(PAGES)} 頁")
