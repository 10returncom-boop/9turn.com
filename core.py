# -*- coding: utf-8 -*-
"""
9Turn 九回錦｜100 頁靜態知識文章網站生成器核心
- 從 content.PAGES 讀取所有頁面定義，套用共用模板輸出 HTML
- 每頁含完整 SEO meta、canonical、Open Graph、JSON-LD(BreadcrumbList)
"""
import os, json, re, glob, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT  = ROOT  # 輸出到網站根目錄

SITE = {
    "name": "9Turn 九回錦｜硬資產典藏平台",
    "short": "9Turn 九回錦",
    "url": "https://9turn.com/",
    "desc": "【九回錦】只玩有價值的資產，時間歷久也不減。三大典藏、九大珍品，專注可穿越市場週期、世代傳承的硬資產典藏平台。",
}

# ---------- 共用導覽（含 MegaMenu 子層） ----------
# subs 為 list[(label,url)]；label 為 "__head__" 時渲染為 mega 分欄標題；
# subs="__FEATURES__" 時由 render_nav 動態組出 50 大功能連結。
NAV = [
    ("首頁", "index.html", []),
    ("品牌理念", "brand/index.html", [("品牌定位","brand/01-positioning.html"),("品牌釋義","brand/02-origin.html"),("品牌哲學","brand/03-philosophy.html"),("品牌短句","brand/04-slogans.html")]),
    ("三大分類", "category/index.html", [("人文典藏","category/humanity.html"),("大地典藏","category/earth.html"),("工業典藏","category/industry.html")]),
    ("九大資產", "asset/index.html", [
        ("__head__","九大珍品主頁"),
        ("典藏藝術品","asset/art.html"),
        ("典藏宅邸／稀有地產","asset/estate.html"),
        ("古董文玩","asset/antique.html"),
        ("珍稀珠寶","asset/jewelry.html"),
        ("經典酒茶","asset/wine-tea.html"),
        ("頂級原木","asset/timber.html"),
        ("經典名錶","asset/watch.html"),
        ("經典樂器","asset/instrument.html"),
        ("珍稀錢幣與珍郵","asset/coin-stamp.html"),
        ("__head__","深度知識專區（每類 22 篇）"),
        ("藝術品深度專區","asset/art/index.html"),
        ("稀有地產深度專區","asset/estate/index.html"),
        ("古董文玩深度專區","asset/antique/index.html"),
        ("珍稀珠寶深度專區","asset/jewelry/index.html"),
        ("經典酒茶深度專區","asset/wine-tea/index.html"),
        ("頂級原木深度專區","asset/timber/index.html"),
        ("經典名錶深度專區","asset/watch/index.html"),
        ("經典樂器深度專區","asset/instrument/index.html"),
        ("錢幣珍郵深度專區","asset/coin-stamp/index.html"),
    ]),
    ("四大準則", "criteria/index.html", [("稀缺性","criteria/scarcity.html"),("底層價值","criteria/value.html"),("完整溯源","criteria/provenance.html"),("長期典藏屬性","criteria/longterm.html")]),
    ("五大服務", "service/index.html", [("資產配置諮詢","service/allocation.html"),("盡職調查","service/due-diligence.html"),("藏家私密媒合","service/matchmaking.html"),("持有規劃","service/holding-plan.html"),("市場觀察","service/market-watch.html")]),
    ("知識體系", "knowledge/index.html", [
        ("藝術鑑賞入門","knowledge/art-appreciation.html"),
        ("地產地段邏輯","knowledge/estate-logic.html"),
        ("文玩鑑定基礎","knowledge/antique-authenticity.html"),
        ("寶石分級認識","knowledge/gem-grading.html"),
        ("酒茶熟成學問","knowledge/wine-aging.html"),
        ("木材溯源課","knowledge/timber-provenance.html"),
        ("名錶機芯入門","knowledge/watch-movement.html"),
        ("樂器聲學原理","knowledge/instrument-acoustics.html"),
        ("錢幣評級指南","knowledge/coin-grading.html"),
        ("資產配置知識","knowledge/asset-allocation.html"),
        ("風險管理學","knowledge/risk-management.html"),
        ("術語表","appendix/glossary.html"),
        ("台灣法規對照","appendix/regulation.html"),
        ("來源查驗指南","appendix/provenance-guide.html"),
        ("持有指南","appendix/holding-guide.html"),
        ("免責聲明","appendix/disclaimer.html"),
        ("常見問答","appendix/faq.html"),
    ]),
    ("網站地圖", "sitemap.html", []),
]

BRAND_SVG = (
    '<svg viewBox="0 0 64 64" aria-hidden="true">'
    '<rect width="64" height="64" rx="14" fill="#0E2A23"/>'
    '<circle cx="32" cy="32" r="20" fill="none" stroke="#C9A227" stroke-width="1.5" opacity=".55"/>'
    '<text x="32" y="41" font-family="Noto Serif TC,serif" font-size="32" font-weight="900" fill="#E2C875" text-anchor="middle">9</text>'
    '</svg>'
)

def _lk(prefix, u):
    return (prefix.rstrip("/") + "/" + u) if prefix else u

def render_nav(prefix):
    lis = []
    for t, u, subs in NAV:
        if subs:
            links = []
            for st, su in subs:
                if st == "__head__":
                    links.append(f'<div class="mega-head">{su}</div>')
                else:
                    links.append(f'<a href="{_lk(prefix, su)}">{st}</a>')
            item = (f'<div class="drop">'
                    f'<a class="drop-a" href="{_lk(prefix,u)}">{t}'
                    f'<svg class="caret" viewBox="0 0 24 24" width="10" height="10" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></a>'
                    f'<div class="mega">{"".join(links)}</div></div>')
        else:
            item = f'<a href="{_lk(prefix,u)}">{t}</a>'
        lis.append(item)
    return f"""<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="{_lk(prefix,'index.html')}">{BRAND_SVG}
      <span class="brand-name">9Turn 九回錦</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-label="開啟選單"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
    <nav class="site-nav" aria-label="主選單">{''.join(lis)}</nav>
  </div>
</header>"""

def icon_svg(name):
    """三大分類／章節使用的簡潔 SVG 圖示"""
    svgs = {
        "humanity": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6c2 0 3 1 3 3v6c-3 1-6 1-6-2V9c0-2 1-3 3-3z"/><path d="M15 12c4 4 8 10 9 16 1 5-3 10-8 10-3 0-5-1-5-1"/><path d="M24 8h14M28 8c1 4 1 8 0 12h8"/></svg>',
        "earth": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c5 0 9 4 9 9 0 2-1 4-2 5-3 1-5 3-5 6v2h4M33 18a7 7 0 0 0-2-14c-4 0-7 3-7 7v3"/><path d="M14 30c-2 1-3 3-3 5 0 3 3 5 6 5 2 0 4-1 5-2"/><circle cx="40" cy="40" r="3"/></svg>',
        "industry": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="24" cy="24" r="12"/><circle cx="24" cy="24" r="4"/><path d="M24 12v4M24 32v4M12 24h4M32 24h4M15.5 15.5l2.8 2.8M29.7 29.7l2.8 2.8M32.5 15.5l-2.8 2.8M18.3 29.7l-2.8 2.8"/></svg>',
        "mark": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="24" cy="24" r="16"/><path d="M24 8v8M24 32v8M8 24h8M32 24h8"/></svg>',
        "seal": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="10" y="10" width="28" height="28" rx="4"/><path d="M10 18h28M10 26h28M18 10v28M26 10v28"/><circle cx="24" cy="34" r="2"/></svg>',
        "scroll": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M14 8h22v26a4 4 0 0 1-4 4h-4a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2h8"/><path d="M14 8a4 4 0 0 0-4 4v20a4 4 0 0 0 4 4h6V12"/><path d="M18 18h12M18 24h8"/></svg>',
    }
    return svgs.get(name, svgs["mark"])

def pillar_svg(cls):
    return icon_svg({"humanity":"humanity","earth":"earth","industry":"industry"}.get(cls,"mark"))

# ---------- 模板函數 ----------
def esc(s):
    return s

def og_image():
    return SITE["url"].rstrip("/") + "/assets/img/og-cover.webp"

def page_jsonld(p):
    """每頁輸出 ≥3 種結構化資料：Organization + WebSite + BreadcrumbList/Article/ItemList + FAQPage"""
    base = SITE["url"].rstrip("/")
    canon = SITE["url"] if p.get("is_root") else base + "/" + p["out_dir"] + "/" + p["file"]
    out = []
    out.append({"@context":"https://schema.org","@type":"Organization",
                "name":SITE["name"],"url":SITE["url"],
                "logo":base+"/assets/img/favicon.svg","sameAs":[]})
    out.append({"@context":"https://schema.org","@type":"WebSite",
                "name":SITE["name"],"url":SITE["url"],"description":SITE["desc"],
                "potentialAction":{"@type":"SearchAction","target":SITE["url"]+"?q={search_term_string}","query-input":"required name=search_term_string"}})
    items = [{"@type":"ListItem","position":i+1,"name":label,
              "item": base + "/" + href.lstrip("./")}
             for i,(label,href) in enumerate(p.get("crumb",[("首頁","index.html")]))]
    out.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items})
    if p.get("is_root"):
        nine = [(n,u) for n,u in NAV[3][2] if n != "__head__"][:9]
        out.append({"@context":"https://schema.org","@type":"ItemList","name":"九大珍品",
                    "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,
                                        "url": base+"/"+u} for i,(n,u) in enumerate(nine)]})
    else:
        out.append({"@context":"https://schema.org","@type":"Article",
                    "headline":p.get("h1",p.get("title")),
                    "description":p.get("desc",SITE["desc"]),
                    "datePublished":p.get("date","2026-01-01"),
                    "dateModified":p.get("date","2026-01-01"),
                    "image":og_image(),
                    "author":{"@type":"Organization","name":SITE["name"]},
                    "publisher":{"@type":"Organization","name":SITE["name"]},
                    "mainEntityOfPage":canon})
    if p.get("faq"):
        out.append({"@context":"https://schema.org","@type":"FAQPage",
                    "mainEntity":[{"@type":"Question","name":q["q"],
                                   "acceptedAnswer":{"@type":"Answer","text":q["a"]}}
                                  for q in p["faq"]]})
    return out

def render_head(p, prefix=""):
    title = p.get("title", SITE["name"])
    desc = p.get("desc", SITE["desc"])
    base = SITE["url"].rstrip("/")
    if p.get("is_root"):
        canon = SITE["url"]
    else:
        canon = base + "/" + p["out_dir"] + "/" + p["file"]
    kw = p.get("kw", "9Turn,九回錦,硬資產,典藏資產,資產配置")
    og = og_image()
    og_type = "website" if p.get("is_root") else p.get("og_type","article")
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="index, follow, max-image-preview:large">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="theme-color" content="#0E2A23">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="zh_TW">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@9turn">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og}">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230E2A23'/%3E%3Ccircle cx='32' cy='32' r='20' fill='none' stroke='%23C9A227' stroke-width='1.5' opacity='.55'/%3E%3Ctext x='32' y='42' font-family='Noto Serif TC,serif' font-size='32' font-weight='900' fill='%23E2C875' text-anchor='middle'%3E9%3C/text%3E%3C/svg%3E">
<link rel="manifest" href="{prefix}manifest.webmanifest">
<link rel="sitemap" type="application/xml" href="{prefix}sitemap.xml">
<link rel="preconnect" href="https://miaoda.feishu.cn">
<link href="https://miaoda.feishu.cn/fonts/css2?family=Noto+Serif+TC:wght@400;600;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/css/style.css">
<script type="application/ld+json">{json.dumps(p.get('jsonld') or page_jsonld(p), ensure_ascii=False)}</script>"""

def crumbs(p):
    parts = []
    for label, href in p.get("crumb", [("首頁","index.html")]):
        parts.append(f'<a href="{href}">{label}</a>')
    return '<span class="sep">›</span>'.join(parts)

def _js(s):
    return s.replace('\\','\\\\').replace('"','\\"').replace('\n',' ')

def depth_prefix(out_dir):
    """依 out_dir 層級組相對路徑前綴：root→''、asset→'../'、asset/art→'../../'"""
    if out_dir in (".", ""):
        return ""
    return "../" * (out_dir.count("/") + 1)

def all_pages():
    """合併 content.PAGES（既有100頁）與 content_deep.PAGES（九大資產深度專區）"""
    import content
    pages = dict(content.PAGES)
    try:
        import content_deep
        pages.update(content_deep.PAGES)
    except ImportError:
        pass
    return pages

def render_index(prefix):
    """每頁內嵌全站索引，供 autocomplete 搜尋與多面向篩選"""
    rows = []
    for sk, p in all_pages().items():
        if p.get("out_dir") in (".", ""):
            u = _lk(prefix, p["file"])
        else:
            u = _lk(prefix, p["out_dir"] + "/" + p["file"])
        rows.append('["%s","%s","%s"]' % (_js(p.get("h1", p.get("title"))), u, _js(p.get("section", ""))))
    return "window.SITE_INDEX=[" + ",".join(rows) + "];"

def render_footer(prefix):
    def col(title, items):
        lis = "".join(f'<a href="{_lk(prefix,u)}">{t}</a>' for t,u in items)
        return f'<div><h5>{title}</h5>{lis}</div>'
    c1 = col("品牌", [("品牌定位","brand/01-positioning.html"),("品牌釋義","brand/02-origin.html"),("品牌哲學","brand/03-philosophy.html"),("品牌短句","brand/04-slogans.html")])
    c2 = col("三大分類", [("人文典藏","category/humanity.html"),("大地典藏","category/earth.html"),("工業典藏","category/industry.html")])
    c3 = col("九大資產", [("典藏藝術品","asset/art.html"),("經典名錶","asset/watch.html"),("珍稀珠寶","asset/jewelry.html"),("九大資產總覽","asset/index.html")])
    c4 = col("資源", [("知識體系","knowledge/index.html"),("術語表","appendix/glossary.html"),("常見問答","appendix/faq.html"),("網站地圖","sitemap.html"),("免責聲明","appendix/disclaimer.html")])
    tags = "".join(f'<a class="tag" href="{_lk(prefix,u)}">{t}</a>'
                   for t,u in [("典藏藝術品","asset/art.html"),("稀有地產","asset/estate.html"),("古董文玩","asset/antique.html"),("珍稀珠寶","asset/jewelry.html"),("經典酒茶","asset/wine-tea.html"),("頂級原木","asset/timber.html"),("經典名錶","asset/watch.html"),("經典樂器","asset/instrument.html"),("錢幣郵票","asset/coin-stamp.html")])
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">{c1}{c2}{c3}{c4}</div>
    <div class="tag-cloud" aria-label="熱門標籤"><span class="tc-title">熱門標籤</span>{tags}</div>
    <div class="footer-note">
      9Turn 九回錦｜只玩有價值的資產。三大典藏、九大珍品，專注可穿越市場週期、世代傳承的硬資產典藏平台。
      本網站內容僅為典藏資產美學與價值研究分享，不構成投資建議或獲利保證；各類硬資產價格會隨市場波動，交易請自行審慎評估。
    </div>
    <div class="copyright">© <span id="year"></span> 9Turn 九回錦｜九回見錦，價值歷循環而不滅</div>
  </div>
</footer>
<div class="search-overlay" hidden aria-hidden="true">
  <div class="search-box" role="dialog" aria-label="全站搜尋">
    <input id="site-search" type="search" placeholder="搜尋資產、功能、知識…" autocomplete="off" aria-autocomplete="list">
    <div class="search-suggest" role="listbox"></div>
  </div>
</div>
<nav class="float-nav" aria-label="站內快捷導航">
  <a class="f-line" href="https://line.me/ti/p/g-FTLSqJAR" target="_blank" rel="noopener" aria-label="加入 LINE 官方帳號"><svg viewBox="0 0 48 48" width="100%" height="100%" aria-hidden="true"><rect width="48" height="48" rx="11" fill="#06C755"/><rect x="8" y="12" width="32" height="21" rx="5" fill="#FFFFFF"/><path d="M16 33.5 L12.5 40.5 L21.5 33.5 Z" fill="#FFFFFF"/><text x="24" y="27" text-anchor="middle" font-size="11" font-weight="700" fill="#06C755" font-family="Arial,Helvetica,sans-serif">LINE</text></svg></a>
  <a class="f-back" href="#" aria-label="回上一頁"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 14 4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 6 6v1"/></svg></a>
  <a class="f-home" href="{_lk(prefix,'index.html')}" aria-label="回首頁"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 10 9-7 9 7"/><path d="M5 9v11h14V9"/></svg></a>
</nav>
<script>{render_index(prefix)}</script>
<script src="{prefix}assets/js/main.js"></script>"""

def page_head(p):
    badge = f'<div class="badge badge-gold">{p["section"]}</div>' if p.get("section") else ''
    return f"""<div class="page-head">
  <div class="container">
    <nav class="crumbs">{crumbs(p)}</nav>
    {badge}
    <h1>{p.get('h1','')}</h1>
    <p class="lede">{p.get('lede','')}</p>
  </div>
</div>"""

def hero(p):
    return f"""<section class="hero" style="background-image:url('assets/img/art.webp')">
  <div class="hero-bg-img" aria-hidden="true"></div>
  <div class="container">
    <div class="hero-inner">
      <div class="hero-text">
        <nav class="crumbs">{crumbs(p)}</nav>
        <p class="eyebrow">HARD ASSET · 硬資產典藏平台</p>
        <h1>{p.get('h1','')}</h1>
        <p class="hero-slogan">【九回錦】只玩有價值的資產，時間歷久也不減</p>
        <p class="tagline">{p.get('lede','')}</p>
        <div class="meta">
          <span>三大典藏 · 九大珍品</span>
          <span>四大篩選準則</span>
          <span>五大全流程服務</span>
        </div>
        <div class="hero-actions">
          <a class="btn btn-gold" href="asset/index.html">9種不賠資產</a>
          <a class="btn btn-gold" href="criteria/index.html">4種秘訣</a>
        </div>
      </div>
    </div>
  </div>
</section>"""

def related_for(p):
    """同資料夾其他頁組成「延伸閱讀」模組"""
    sibs = [(pg["file"], pg.get("h1", pg.get("title")))
            for sk, pg in all_pages().items()
            if pg["out_dir"] == p["out_dir"] and pg["file"] != p["file"]]
    if not sibs:
        return ""
    cards = "".join(f'<a class="rel-card" href="{pgf}"><span class="rc-tag">{p.get("section","")}</span><span class="rc-title">{t}</span></a>' for pgf, t in sibs[:6])
    return f'<section class="related" aria-label="延伸閱讀"><h2>延伸閱讀</h2><div class="rel-grid">{cards}</div></section>'

def treemap(prefix):
    """側欄 Treemap 樹狀地圖：依 NAV 站點結構生成可摺疊導覽樹（2 層內）"""
    li = []
    for t, u, subs in NAV:
        if subs:
            heads = [(st, su) for st, su in subs if st != "__head__"]
            kids = "".join(f'<li><a href="{_lk(prefix,su)}">{st}</a></li>' for st, su in heads)
            li.append(f'<details class="tr-node" open><summary><a href="{_lk(prefix,u)}">{t}</a></summary><ul>{kids}</ul></details>')
        else:
            li.append(f'<a class="tr-leaf" href="{_lk(prefix,u)}">{t}</a>')
    return f'<nav class="treemap" aria-label="站點樹狀地圖"><h4>站點地圖</h4>{"".join(li)}</nav>'

def page_template(p):
    inner = p["body"]
    prefix = depth_prefix(p.get("out_dir"))
    if p.get("is_root"):
        top = hero(p)
    else:
        top = page_head(p)
    related = related_for(p)
    if p.get("layout") == "2col":
        body_html = f"""<div class="layout-2col">
  <main class="article">{inner}{related}</main>
  <aside class="sidebar">
    <div class="toc" data-toc><h4>本頁目錄</h4><ol></ol></div>
    {treemap(prefix)}
    {p.get('sidebar_html','')}
    <button class="save-btn" data-save type="button" aria-pressed="false"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 21s-7-4.4-9.3-8.5C.7 9 2.5 5 6.2 5c2 0 3.2 1.2 5.8 3.8C14.6 6.2 15.8 5 17.8 5c3.7 0 5.5 4 3.5 7.5C19 16.6 12 21 12 21z"/></svg><span>收藏本頁</span></button>
  </aside>
</div>"""
    else:
        body_html = f"""<div class="container"><main class="article">{inner}{related}</main></div>"""
    pager = ""
    if p.get("prev") or p.get("next"):
        parts = []
        if p.get("prev"):
            parts.append(f'<a href="{p["prev"][1]}"><span class="dir">← 上一篇</span><span class="t">{p["prev"][0]}</span></a>')
        if p.get("next"):
            parts.append(f'<a href="{p["next"][1]}"><span class="dir">下一篇 →</span><span class="t">{p["next"][0]}</span></a>')
        pager = f'<nav class="pager">{"".join(parts)}</nav>'
    html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
{render_head(p, prefix)}
</head>
<body>
{render_nav(prefix)}
{top}
{body_html}
{pager}
{render_footer(prefix)}
</body>
</html>"""
    return html

def build_seo(plan):
    """產生 sitemap.xml / robots.txt / manifest.webmanifest / 404.html，並為每個子資料夾複製自含 SEO 檔（搬移獨立）"""
    base = SITE["url"].rstrip("/")
    items = ""
    for d, p in plan:
        u = SITE["url"] if p.get("is_root") else base + "/" + p["out_dir"] + "/" + p["file"]
        prio = 1.0 if p.get("is_root") else (0.8 if p.get("section") == "50大功能" else 0.7)
        items += (f'<url><loc>{u}</loc><lastmod>{SITE.get("date","2026-10-14")}</lastmod>'
                  f'<changefreq>weekly</changefreq><priority>{prio}</priority></url>')
    smap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + items + '</urlset>')
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(smap)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n")
    manifest = json.dumps({
        "name": SITE["name"], "short_name": "9Turn 九回錦", "start_url": "index.html",
        "display": "standalone", "background_color": "#F5F1E8", "theme_color": "#0E2A23",
        "lang": "zh-Hant",
        "icons": [{"src": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230E2A23'/%3E%3Ctext x='32' y='42' font-family='serif' font-size='32' font-weight='900' fill='%23E2C875' text-anchor='middle'%3E9%3C/text%3E%3C/svg%3E",
                   "sizes": "any", "type": "image/svg+xml", "purpose": "any"}],
    }, ensure_ascii=False)
    with open(os.path.join(OUT, "manifest.webmanifest"), "w", encoding="utf-8") as f:
        f.write(manifest)
    # 每個子資料夾內自含 manifest + sitemap（列出該資料夾頁面），搬移時仍獨立成站
    subdirs = sorted({d for d, _ in plan if os.path.abspath(d) != os.path.abspath(OUT)})
    for sd in subdirs:
        os.makedirs(sd, exist_ok=True)
        with open(os.path.join(sd, "manifest.webmanifest"), "w", encoding="utf-8") as f:
            f.write(manifest)
        sub = ""
        for d, p in plan:
            if d == sd and not p.get("is_root"):
                sub += (f'<url><loc>{base}/{p["out_dir"]}/{p["file"]}</loc>'
                        f'<lastmod>{SITE.get("date","2026-10-14")}</lastmod>'
                        f'<changefreq>weekly</changefreq><priority>0.7</priority></url>')
        sub_smap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + sub + '</urlset>')
        with open(os.path.join(sd, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(sub_smap)
    # 404 頁
    p404 = {"out_dir": ".", "file": "404.html", "is_root": False, "section": "",
            "title": "404｜頁面不存在 — 9Turn 九回錦", "h1": "這頁跑到別的地方去了",
            "desc": "找不到你要的頁面。返回 9Turn 九回錦首頁，繼續探索三大典藏與九大珍品。",
            "kw": "9Turn,404,找不到頁面",
            "crumb": [("首頁", "index.html")],
            "lede": "網址可能打錯、頁面被搬動，或連結已過期。別擔心，價值不會消失。",
            "body": '<p>回到首頁，或從上方導覽重新出發：三大典藏、九大珍品、四大準則，都在等著你。</p>'
                    '<p class="cta-row"><a class="btn btn-gold" href="index.html">回到首頁</a>'
                    '<a class="btn btn-ghost" href="asset/index.html">探索九大資產</a></p>',
        }
    html404 = page_template(p404)
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(html404)
    print("[seo] sitemap.xml / robots.txt / manifest.webmanifest / 404.html 已生成")

def build_sitemap_page(pages):
    """組出全站地圖頁（sitemap.html）：依目錄分群列出所有頁面連結"""
    order = [
        (".", "首頁"),
        ("brand", "品牌理念"),
        ("category", "三大分類"),
        ("asset", "九大資產主頁"),
        ("criteria", "四大準則"),
        ("service", "五大服務"),
        ("knowledge", "知識體系"),
    ]
    buckets = {}
    for p in pages.values():
        k = "knowledge" if p["out_dir"] == "appendix" else p["out_dir"]
        buckets.setdefault(k, []).append(p)
    deep = sorted([od for od in buckets if od.startswith("asset/")])
    def link_of(p):
        u = p["file"] if p["out_dir"] in (".", "") else p["out_dir"] + "/" + p["file"]
        return f'<a href="{u}">{p.get("h1", p.get("title"))}</a>'
    blocks = []
    for od, label in order:
        if od in buckets:
            items = "".join(link_of(p) for p in sorted(buckets[od], key=lambda x: x["file"]))
            blocks.append(f'<div class="box"><h4>{label}（{len(buckets[od])} 頁）</h4>{items}</div>')
    for od in deep:
        label = buckets[od][0].get("deep_name", od)
        items = "".join(link_of(p) for p in sorted(buckets[od], key=lambda x: x["file"]))
        blocks.append(f'<div class="box"><h4>{label}（{len(buckets[od])} 篇）</h4>{items}</div>')
    total = len(pages) + 1
    body = ('<p>本網站共計 <strong>' + str(total) + '</strong> 個頁面。下方依分類列出全部連結，從這裡可以抵達任何一篇知識文章。</p>'
            '<div class="sitemap-grid">' + "".join(blocks) + "</div>")
    return {
        "out_dir": ".", "file": "sitemap.html",
        "title": f"網站地圖｜9Turn 九回錦 全部 {total} 頁導覽",
        "desc": f"9Turn 九回錦網站地圖：一次看完品牌理念、三大分類、九大資產深度專區、四大準則、五大服務與知識體系，共 {total} 頁。",
        "kw": "9Turn,九回錦,網站地圖,sitemap,硬資產,典藏資產",
        "section": "網站地圖",
        "crumb": [("首頁", "index.html"), ("網站地圖", "sitemap.html")],
        "h1": "網站地圖：硬資產知識全覽導覽",
        "lede": "從品牌理念到九大資產的深度專區，全部頁面連結都在這。想找什麼，直接點。",
        "body": body,
    }

def build_all():
    pages = all_pages()
    pages["sitemap"] = build_sitemap_page(pages)
    dirs = set()
    plan = []
    for slug, p in pages.items():
        d = os.path.join(OUT, p["out_dir"])
        dirs.add(d)
        plan.append((d, p))
    # 第一遍：統一清理各目錄既有 html，避免改名後殘留或互刪
    for d in dirs:
        for old in glob.glob(os.path.join(d, "*.html")):
            os.remove(old)
    # 每個子資料夾內自含 assets，搬移資料夾時仍可獨立成站
    def sync_assets(d):
        if os.path.abspath(d) == os.path.abspath(OUT):
            return
        ad = os.path.join(d, "assets")
        os.makedirs(os.path.join(ad, "css"), exist_ok=True)
        os.makedirs(os.path.join(ad, "js"), exist_ok=True)
        os.makedirs(os.path.join(ad, "img"), exist_ok=True)
        for rel in ["css/style.css", "js/main.js"]:
            shutil.copy(os.path.join(OUT, "assets", rel), os.path.join(ad, rel))
        for img in glob.glob(os.path.join(OUT, "assets", "img", "*")):
            shutil.copy(img, os.path.join(ad, "img", os.path.basename(img)))
    for d in dirs:
        sync_assets(d)
    # 第二遍：全部重建
    for d, p in plan:
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, p["file"])
        html = page_template(p)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[build] {p['out_dir']}/{p['file']}  ({len(html)} bytes)")
    build_seo(plan)

if __name__ == "__main__":
    build_all()
    print("done")
