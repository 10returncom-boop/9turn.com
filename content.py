# -*- coding: utf-8 -*-
"""
9Turn 九回錦｜100 頁內容定義（第一部分：首頁、品牌、三大分類）
"""
import core

PAGES = {}

# ============================================================
# 首頁
# ============================================================
PAGES["index"] = {
    "out_dir": ".", "file": "index.html", "is_root": True,
    "title": "9Turn 九回錦｜只玩有價值的資產 — 硬資產典藏平台",
    "desc": "9Turn 九回錦是專注硬資產的典藏平台，涵蓋人文、大地、工業三大典藏與九大珍品。只經營具備底層稀缺性、可穿越市場週期、世代傳承的資產。",
    "kw": "9Turn,九回錦,硬資產,典藏資產,資產配置,世代傳承,典藏藝術品,珍稀珠寶",
    "h1": "只玩<em>有價值</em>的資產",
    "lede": "9Turn 九回錦｜三大典藏、九大珍品。我們不玩短線炒作，只經營具備底層稀缺性、可穿越市場週期、世代傳承的硬資產。九回見錦，價值歷循環而不滅。",
    "section": "品牌首頁",
    "body": """
<section>
  <div class="container">
    <div class="sec-head">
      <p class="eyebrow">三大分類 × 九大資產</p>
      <h2>一盤看懂我們的典藏版圖</h2>
      <p class="lede">將九大典藏資產依價值屬性分為三大維度，協助藏家做資產配置佈局。每樣資產都經過四大準則審核，才進得了典藏名單。</p>
    </div>
    <div class="pillar-row">
      <div class="pillar humanity"><img src="assets/img/art.webp" alt="人文典藏滿版配圖" loading="lazy"><div class="pillar-icon">{icon0}</div><h3>人文典藏</h3><div class="pillar-zh">HUMANITY</div><p>人類創作與歷史痕跡——典藏藝術品、典藏宅邸／稀有地產、古董文玩。</p><div class="count">3 大珍品</div></div>
      <div class="pillar earth"><img src="assets/img/timber.webp" alt="大地典藏滿版配圖" loading="lazy"><div class="pillar-icon">{icon1}</div><h3>大地典藏</h3><div class="pillar-zh">EARTH</div><p>自然原生稀缺物——珍稀珠寶、經典酒茶、頂級原木與珍稀木材。</p><div class="count">3 大珍品</div></div>
      <div class="pillar industry"><img src="assets/img/watch.webp" alt="工業典藏滿版配圖" loading="lazy"><div class="pillar-icon">{icon2}</div><h3>工業典藏</h3><div class="pillar-zh">INDUSTRY</div><p>經典工藝造物——經典名錶、經典樂器、珍稀錢幣與典藏珍郵。</p><div class="count">3 大珍品</div></div>
    </div>
  </div>
</section>

<section style="background:var(--ivory-2)">
  <div class="container">
    <div class="sec-head">
      <p class="eyebrow">九大硬資產</p>
      <h2>穿越市場週期的珍品清單</h2>
      <p class="lede">從藝術品到稀有地產、從珠寶到名錶，每樣都是「供給有限、無法量產」的底層稀缺資產。</p>
    </div>
    <div class="card-grid">
      <div class="card"><img src="assets/img/art.webp" alt="典藏藝術品滿版配圖" loading="lazy"><span class="num">01</span><h3>典藏藝術品</h3><p>有完整來源、展覽與出版紀錄的原作，承載藝術史脈絡。</p><a class="card-link" href="asset/art.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/estate.webp" alt="典藏宅邸稀有地產滿版配圖" loading="lazy"><span class="num">02</span><h3>典藏宅邸／稀有地產</h3><p>地段稀缺、建築具設計或歷史價值、供給難以複製。</p><a class="card-link" href="asset/estate.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/antique.webp" alt="古董文玩滿版配圖" loading="lazy"><span class="num">03</span><h3>古董文玩</h3><p>傳世有序、鑑定完整的古器物與文房雅藏。</p><a class="card-link" href="asset/antique.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/jewelry.webp" alt="珍稀珠寶滿版配圖" loading="lazy"><span class="num">04</span><h3>珍稀珠寶</h3><p>天然寶石、古董珠寶、大師設計典藏，附國際鑑定證書。</p><a class="card-link" href="asset/jewelry.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/wine-tea.webp" alt="經典酒茶滿版配圖" loading="lazy"><span class="num">05</span><h3>經典酒茶</h3><p>頂級陳年酒與典藏老茶，仰賴風土與長期熟成。</p><a class="card-link" href="asset/wine-tea.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/timber.webp" alt="頂級原木滿版配圖" loading="lazy"><span class="num">06</span><h3>頂級原木</h3><p>生長週期長、原生資源枯竭的珍貴大料，來源可追溯。</p><a class="card-link" href="asset/timber.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/watch.webp" alt="經典名錶滿版配圖" loading="lazy"><span class="num">07</span><h3>經典名錶</h3><p>限量、全套保卡與維修紀錄的經典機械腕錶。</p><a class="card-link" href="asset/watch.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/instrument.webp" alt="經典樂器滿版配圖" loading="lazy"><span class="num">08</span><h3>經典樂器</h3><p>名家手工製作的提琴、古典吉他，重視聲學品質與來源。</p><a class="card-link" href="asset/instrument.html">深入了解 →</a></div>
      <div class="card"><img src="assets/img/coin.webp" alt="珍稀錢幣與珍郵滿版配圖" loading="lazy"><span class="num">09</span><h3>珍稀錢幣與珍郵</h3><p>古錢、珍稀金銀幣、初版罕見郵票，重視版別與品相。</p><a class="card-link" href="asset/coin-stamp.html">深入了解 →</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head">
      <p class="eyebrow">價值篩選四大準則</p>
      <h2>不是貴的就算資產，過得了這四關才算</h2>
    </div>
    <div class="card-grid">
      <div class="card card-feature"><img src="assets/img/timber.webp" alt="稀缺性準則配圖" loading="lazy"><span class="num">壹</span><h3>稀缺性</h3><p>供給有限，無法量產複製。</p></div>
      <div class="card card-feature"><img src="assets/img/art.webp" alt="底層價值準則配圖" loading="lazy"><span class="num">貳</span><h3>底層價值</h3><p>具備美學、歷史、工藝、材料或土地本質價值，不受短期熱潮牽制。</p></div>
      <div class="card card-feature"><img src="assets/img/watch.webp" alt="完整溯源準則配圖" loading="lazy"><span class="num">參</span><h3>完整溯源</h3><p>來源清晰，文件脈絡齊全，可追溯。</p></div>
      <div class="card card-feature"><img src="assets/img/jewelry.webp" alt="長期典藏屬性準則配圖" loading="lazy"><span class="num">肆</span><h3>長期典藏屬性</h3><p>適合持有、傳承，具備穩定的長期流通基礎。</p></div>
    </div>
    <p style="text-align:center;margin-top:26px"><a class="btn btn-outline" href="criteria/index.html">看完整審核邏輯</a></p>
  </div>
</section>

<section style="background:var(--ivory-2)">
  <div class="container">
    <div class="sec-head">
      <p class="eyebrow">硬資產典藏</p>
      <h2>把「典藏」這件事，做成一套完整系統</h2>
      <p class="lede">從品牌哲學、九大資產知識、四大準則，到五大服務與知識體系，九回錦用三大典藏、九大珍品與完整知識庫，建構專業的硬資產典藏體驗。</p>
    </div>
    <p style="text-align:center;margin-top:26px"><a class="btn btn-gold" href="asset/index.html">探索九大資產</a></p>
  </div>
</section>

<div class="appendix-band">
  <div class="container">
    <div class="grid">
      <div><h2>九回見錦，價值歷循環而不滅</h2><p style="color:rgba(247,243,234,.8)">真正的價值，會在時間輪轉之後浮現。我們陪你用對的方法，把資產一代一代傳下去。</p></div>
      <div><a class="btn btn-gold" href="service/index.html">了解全流程典藏服務</a></div>
    </div>
  </div>
</div>
""".format(icon0=core.pillar_svg("humanity"), icon1=core.pillar_svg("earth"), icon2=core.pillar_svg("industry")),
}

# ============================================================
# 品牌理念
# ============================================================
def brand_side(current):
    items = [
        ("品牌定位：只玩有價值的資產", "01-positioning.html", "positioning"),
        ("品牌釋義：9Turn 九回錦", "02-origin.html", "origin"),
        ("價值哲學：時間輪轉", "03-philosophy.html", "philosophy"),
        ("品牌短句與口號", "04-slogans.html", "slogans"),
    ]
    lis = []
    for t,u,k in items:
        cls = "active" if k == current else ""
        lis.append(f'<li><a class="{cls}" href="{u}">{t}</a></li>')
    return '<div class="box"><img class="box-img" src="assets/img/brand.webp" alt="品牌理念" loading="lazy"><h4>品牌理念</h4><ul>' + "".join(lis) + "</ul></div>"

PAGES["brand-index"] = {
    "out_dir": "brand", "file": "index.html",
    "title": "品牌理念｜9Turn 九回錦 硬資產典藏平台",
    "desc": "9Turn 九回錦品牌理念：品牌定位、釋義、價值哲學與品牌短句。只玩有價值的資產，九回見錦，價值歷循環而不滅。",
    "kw": "9Turn,九回錦,品牌定位,品牌釋義,價值哲學,硬資產",
    "section": "品牌理念",
    "crumb": [("首頁","../index.html"), ("品牌理念","../brand/index.html")],
    "h1": "品牌理念：為什麼我們「只玩有價值的資產」？",
    "lede": "9Turn 中 9 對應九大典藏資產，Turn 代表市場輪轉與週期；「九回錦」取歷經九次輪轉之後，方能看見珍貴錦緞之意。",
    "layout": "2col",
    "sidebar_html": brand_side("index"),
    "prev": ("首頁","../index.html"),
    "next": ("品牌定位","01-positioning.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/brand.webp" alt="9Turn 九回錦品牌理念：只玩有價值的資產" loading="lazy" width="800" height="600"><figcaption>品牌理念｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 一句話看懂九回錦</h2>
<p>9Turn 九回錦，是專注「硬資產」的典藏平台。硬資產的意思很簡單：它不會因為炒作退燒就消失，它穿越市場週期、可以一代一代傳下去——藝術品、稀有地產、古董文玩、珍稀珠寶、經典酒茶、頂級原木、經典名錶、經典樂器、珍稀錢幣與珍郵，這些都算。</p>
<p>我們不做短線炒作，只經營具備<strong>底層稀缺性</strong>的珍品。用大白話講：<strong>貴不等於資產，能傳下去的才叫資產。</strong></p>

<h2>2. 品牌名的兩個字拆開看</h2>
<table>
<colgroup><col style="width:20%"><col style="width:40%"><col style="width:40%"></colgroup>
<thead><tr><th>字</th><th>字面意思</th><th>對應的資產邏輯</th></tr></thead>
<tbody>
<tr><td><strong>9</strong></td><td>九大典藏資產</td><td>一盤完整的硬資產配置，人文、大地、工業各佔三樣。</td></tr>
<tr><td><strong>Turn</strong></td><td>市場輪轉與週期</td><td>價值在一次次輪轉中沉澱，不靠短線靠長線。</td></tr>
<tr><td><strong>九回錦</strong></td><td>九次輪轉見錦緞</td><td>歷經循環之後，真價值才浮現——這就是品牌信仰。</td></tr>
</tbody>
</table>

<h2>3. 我們相信的三件事</h2>
<ul>
  <li><strong>底層稀缺性勝過一時熱度：</strong>炒上去的會跌回來，稀缺的會一直稀缺。</li>
  <li><strong>完整溯源是價值的通行證：</strong>來源清楚、文件齊全的資產，才值得長期持有。</li>
  <li><strong>典藏是給下一代的事：</strong>不只保值，更是家族資產的代代相傳。</li>
</ul>

<h2>4. 認識九大資產前，先記住這句話</h2>
<blockquote>三大典藏、九大珍品，只玩有價值的資產。人文、大地、工藝，三維佈局典藏資產。九回見錦，價值歷循環而不滅。</blockquote>
<p>準備好走進硬資產的世界了嗎？下一頁，我們從品牌定位開始，一步步帶你看懂這套系統。</p>
""",
}

PAGES["brand-positioning"] = {
    "out_dir": "brand", "file": "01-positioning.html",
    "title": "品牌定位｜9Turn 只玩有價值的資產 是什麼意思",
    "desc": "9Turn 九回錦品牌定位解析：硬資產典藏平台、不做短線炒作、只經營具備底層稀缺性的珍品。看懂我們為什麼這樣定位。",
    "kw": "9Turn,九回錦,品牌定位,硬資產,短線炒作,底層稀缺性",
    "section": "品牌理念",
    "crumb": [("首頁","../index.html"), ("品牌理念","../brand/index.html"), ("品牌定位","../brand/01-positioning.html")],
    "h1": "品牌定位：為什麼我們只玩有價值的資產？",
    "lede": "一句話道盡 9Turn 的存在理由——我們是硬資產典藏平台，專注可穿越市場週期、世代傳承的珍品。",
    "layout": "2col",
    "sidebar_html": brand_side("positioning"),
    "prev": ("品牌理念總覽","index.html"),
    "next": ("品牌釋義","02-origin.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/brand.webp" alt="9Turn 九回錦品牌定位：只玩有價值的資產" loading="lazy" width="800" height="600"><figcaption>品牌定位｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 我們的定位是什麼？一句話講完</h2>
<p>9Turn 九回錦的定位一句話講完：<strong>硬資產典藏平台，專注可穿越市場週期、世代傳承的珍品。</strong></p>
<p>硬資產（Hard Asset）不是金融產品、不是加密貨幣，而是<strong>看得見、摸得著、放得久</strong>的實體珍品。它承載美學、歷史、工藝與材料本質，就算金融市場上上下下，它的底層價值不會憑空消失。</p>

<h2>2. 我們「不做」什麼，為什麼比「做什麼」更重要？</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>我們不做</th><th>我們為什麼不做的理由</th></tr></thead>
<tbody>
<tr><td>不做短線炒作</td><td>熱潮來得快、去得也快，追高進場的人到頭來都是接盤的。真正的價值不在於一時漲跌。</td></tr>
<tr><td>不碰日常消費型資產</td><td>能稱得上「典藏」的，必須有底層稀缺性與長期持有價值；日常用品再貴也不算。</td></tr>
<tr><td>不經營來源不明的標的</td><td>來源不清、文件不齊的資產，就像沒有戶口的房子，價值再高也難以傳承。</td></tr>
</tbody>
</table>

<h2>3. 定位背後，靠哪三個信念撐著？</h2>
<h3>3.1 貴的東西，為什麼不等於資產？</h3>
<p>很多人買了貴的東西，以為自己買到了資產。其實只要它無法穿越市場週期、無法世代傳承，它就是一筆消費，不是資產。</p>
<h3>3.2 為什麼稀缺是硬道理？</h3>
<p>能量產複製的，永遠輪不到你當主角。真正值得典藏的，是「供給有限、無法複製」的珍品。</p>
<h3>3.3 時間為什麼站在我們這邊？</h3>
<p>短線靠運氣，長線靠底層價值。九回錦選擇站在時間這一邊，等價值在輪轉後浮現。</p>

<h2>4. 一句話記住：我們的定位是什麼</h2>
<div class="callout"><div class="ico">◎</div><div><strong>只玩有價值的資產。</strong>這就是 9Turn 九回錦的全部答案。</div></div>
""",
}

PAGES["brand-origin"] = {
    "out_dir": "brand", "file": "02-origin.html",
    "title": "品牌釋義｜9Turn 九回錦 名字背後的哲學",
    "desc": "9Turn 九回錦名字釋義：9 對應九大典藏資產，Turn 代表市場輪轉與週期，九回錦意指歷經九次輪轉方能看見珍貴錦緞。",
    "kw": "9Turn,九回錦,品牌釋義,九大資產,市場輪轉,價值哲學",
    "section": "品牌理念",
    "crumb": [("首頁","../index.html"), ("品牌理念","../brand/index.html"), ("品牌釋義","../brand/02-origin.html")],
    "h1": "品牌釋義：9Turn 這個名字，為什麼藏著價值哲學？",
    "lede": "每個好品牌都有個好名字。九回錦的名字，藏著我們對「價值」最深的相信。",
    "layout": "2col",
    "sidebar_html": brand_side("origin"),
    "prev": ("品牌定位","01-positioning.html"),
    "next": ("價值哲學","03-philosophy.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/brand.webp" alt="9Turn 九回錦品牌釋義：名字背後的價值哲學" loading="lazy" width="800" height="600"><figcaption>品牌釋義｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 「9」：為什麼是九大典藏資產？</h2>
<p>9Turn 的 <strong>9</strong>，對應的就是我們的<strong>九大典藏資產</strong>：典藏藝術品、典藏宅邸／稀有地產、古董文玩、珍稀珠寶、經典酒茶、頂級原木與珍稀木材、經典名錶、經典樂器、珍稀錢幣與典藏珍郵。</p>
<p>為什麼是九個？因為九是「最大」的單數，象徵圓滿與完整。一盤九珍，就是一套完整的硬資產配置。</p>

<h2>2. 「Turn」：市場為什麼一定會輪轉？</h2>
<p>第二個字 <strong>Turn</strong>，講的是<strong>市場的輪轉與週期</strong>。沒有資產能永遠只漲不跌，市場一定會有輪轉、有週期、有起伏。</p>
<p>關鍵不在於躲開輪轉，而在於——<em>在輪轉之後，你的資產還在不在、值不值。</em></p>

<h2>3. 「九回錦」：九次輪轉之後，為什麼才看得見錦緞？</h2>
<div class="callout"><div class="ico">❖</div><div><strong>「九回錦」取歷經九次輪轉之後，方能看見珍貴錦緞之意。</strong>錦，是絲綢中最珍貴的一種；它經得起歲月，越放越顯質地。</div></div>
<p>我們用「九回錦」三個字，向每一位藏家傳遞一個信念：<em>真正的價值，會在時間輪轉之後浮現。</em></p>

<h2>4. 名字與做法，為什麼能對得起來？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:38%"><col style="width:38%"></colgroup>
<thead><tr><th>元素</th><th>字面意思</th><th>我們的落實</th></tr></thead>
<tbody>
<tr><td>9</td><td>九大典藏資產</td><td>三大分類 × 九大珍品，一盤完整佈局</td></tr>
<tr><td>Turn</td><td>市場輪轉與週期</td><td>不做短線炒作，等價值浮現</td></tr>
<tr><td>九回錦</td><td>九次輪轉見錦緞</td><td>世代傳承，長期典藏</td></tr>
</tbody>
</table>

<h2>5. 名字怎麼變成你的記憶點？</h2>
<p>下次聽到 9Turn 九回錦，請記得：<strong>這是一間相信時間、相信稀缺、相信傳承的硬資產典藏平台。</strong></p>
""",
}

PAGES["brand-philosophy"] = {
    "out_dir": "brand", "file": "03-philosophy.html",
    "title": "價值哲學｜時間輪轉 為何價值會浮現",
    "desc": "9Turn 九回錦價值哲學：時間輪轉的意義、為何真價值在週期後浮現、如何用時間檢驗資產。看懂硬資產的長期邏輯。",
    "kw": "9Turn,九回錦,價值哲學,時間輪轉,市場週期,長期典藏",
    "section": "品牌理念",
    "crumb": [("首頁","../index.html"), ("品牌理念","../brand/index.html"), ("價值哲學","../brand/03-philosophy.html")],
    "h1": "價值哲學：真正的價值，為什麼會在時間輪轉後浮現？",
    "lede": "這是九回錦最核心的一句信仰。這頁，我們把這句話講透。",
    "layout": "2col",
    "sidebar_html": brand_side("philosophy"),
    "prev": ("品牌釋義","02-origin.html"),
    "next": ("品牌短句","04-slogans.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/brand.webp" alt="9Turn 九回錦價值哲學：時間輪轉後真價值浮現" loading="lazy" width="800" height="600"><figcaption>價值哲學｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 市場為什麼一定會輪轉？</h2>
<p>市場從不靜止。資金會移動、熱潮會退、利率會變、人心會累。每一次輪轉，就像一次大浪淘沙——<strong>把靠運氣漲上去的洗掉，把靠底層價值站穩的留下。</strong></p>

<h2>2. 為什麼「真價值」會在輪轉後浮現？</h2>
<p>短線市場看的是<strong>情緒與資金</strong>，長線看的是<strong>稀缺與品質</strong>。情緒會散，品質不會。所以當一輪炒作過去、市場冷靜下來，真正稀缺的資產價格會被重新發現——這就是價值浮現的時刻。</p>

<h2>3. 時間為什麼是最公平的考官？</h2>
<table>
<colgroup><col style="width:18%"><col style="width:28%"><col style="width:54%"></colgroup>
<thead><tr><th>週期</th><th>靠什麼定價</th><th>結果</th></tr></thead>
<tbody>
<tr><td>短期</td><td>靠熱度</td><td>追高者進場，價格偏離底層價值。</td></tr>
<tr><td>中期</td><td>靠品質</td><td>市場冷卻，缺乏底層價值的標的開始回落。</td></tr>
<tr><td>長期</td><td>靠稀缺</td><td>真稀缺的珍品被重新定價，價值浮現並沉澱。</td></tr>
<tr><td>世代</td><td>靠傳承</td><td>價值成為家族資產，一代傳一代。</td></tr>
</tbody>
</table>

<h2>4. 這套哲學，怎麼落實在九回錦？</h2>
<ul>
  <li><strong>四大準則審核：</strong>每個標的都先問——稀缺嗎？有底層價值嗎？溯源完整嗎？能長期持有嗎？</li>
  <li><strong>不做短線炒作：</strong>熱門不代表該買，不符合準則的一律不納入。</li>
  <li><strong>強調傳承：</strong>把典藏當成給下一代的事，而不只是這一季的行情。</li>
</ul>

<h2>5. 一句話帶走：時間站在誰那邊？</h2>
<div class="callout"><div class="ico">❖</div><div><strong>時間輪轉，珍品自成錦。</strong>我們選擇和時間站在一起。</div></div>
""",
}

PAGES["brand-slogans"] = {
    "out_dir": "brand", "file": "04-slogans.html",
    "title": "品牌短句與口號｜九回錦 品牌金句大全",
    "desc": "9Turn 九回錦品牌短句與口號整理：三大典藏九大珍品、三維佈局、九回見錦等品牌金句一次看齊，用於對外溝通與SEO。",
    "kw": "9Turn,九回錦,品牌短句,品牌口號,金句,三大典藏,九大珍品",
    "section": "品牌理念",
    "crumb": [("首頁","../index.html"), ("品牌理念","../brand/index.html"), ("品牌短句","../brand/04-slogans.html")],
    "h1": "品牌短句與口號：一開口，為什麼要能講出我們是誰？",
    "lede": "好品牌要有一句能被記住的話。這裡整理九回錦的核心短句，也是我們對外溝通的語言。",
    "layout": "2col",
    "sidebar_html": brand_side("slogans"),
    "prev": ("價值哲學","03-philosophy.html"),
    "next": ("三大分類總覽","../category/index.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/brand.webp" alt="9Turn 九回錦品牌短句與口號" loading="lazy" width="800" height="600"><figcaption>品牌短句與口號｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 主標：最核心的一句，為什麼是它？</h2>
<blockquote>9Turn 九回錦｜只玩有價值的資產</blockquote>
<p>這是九回錦的品牌主標。它同時回答了三個問題：<strong>我們是誰（9Turn 九回錦）、我們做什麼（玩資產）、我們只玩哪種（有價值的）。</strong></p>

<h2>2. 四大品牌短句，各自在說什麼？</h2>
<table>
<colgroup><col style="width:34%"><col style="width:66%"></colgroup>
<thead><tr><th>短句</th><th>含意</th></tr></thead>
<tbody>
<tr><td>三大典藏，九大珍品，只玩有價值的資產</td><td>一盤佈局總覽，把我們的範圍一次講清。</td></tr>
<tr><td>人文、大地、工藝，三維佈局典藏資產</td><td>三大分類的價值維度，配置的骨架。</td></tr>
<tr><td>九回見錦，價值歷循環而不滅</td><td>品牌哲學的濃縮，時間與價值的信仰。</td></tr>
<tr><td>時間輪轉，珍品自成錦</td><td>最詩意的一句，適合傳承與典藏情境。</td></tr>
</tbody>
</table>

<h2>3. 這些短句，用在哪裡？</h2>
<ul>
  <li><strong>首頁 Hero：</strong>用主標＋「三大典藏 · 九大珍品」。</li>
  <li><strong>品牌頁：</strong>用「九回見錦，價值歷循環而不滅」做收尾。</li>
  <li><strong>SEO 標題：</strong>把「硬資產」「典藏資產」「資產配置」等關鍵字織進短句。</li>
  <li><strong>頁尾與文宣：</strong>用「時間輪轉，珍品自成錦」強化品牌記憶。</li>
</ul>

<h2>4. 一句話帶走：為什麼要記住九回見錦？</h2>
<div class="callout"><div class="ico">◎</div><div><strong>九回見錦，價值歷循環而不滅。</strong>這句話，值得你記住九回錦。</div></div>
""",
}

# ============================================================
# 三大分類
# ============================================================
def category_side(current):
    items = [("三大分類總覽","index.html","index"),
             ("人文典藏","humanity.html","humanity"),
             ("大地典藏","earth.html","earth"),
             ("工業典藏","industry.html","industry")]
    lis = []
    for t,u,k in items:
        cls = "active" if k == current else ""
        lis.append(f'<li><a class="{cls}" href="{u}">{t}</a></li>')
    return '<div class="box"><img class="box-img" src="assets/img/category.webp" alt="三大分類" loading="lazy"><h4>三大分類</h4><ul>' + "".join(lis) + "</ul></div>"

PAGES["category-index"] = {
    "out_dir": "category", "file": "index.html",
    "title": "三大分類｜人文 大地 工業 典藏資產怎麼分",
    "desc": "9Turn 九回錦三大分類：人文典藏、大地典藏、工業典藏。看懂九大硬資產如何依價值屬性分為三大維度，做好資產配置佈局。",
    "kw": "9Turn,九回錦,三大分類,人文典藏,大地典藏,工業典藏,資產配置",
    "section": "三大分類",
    "crumb": [("首頁","../index.html"), ("三大分類","../category/index.html")],
    "h1": "三大分類：九大資產，為什麼要先放對位置？",
    "lede": "將九大典藏資產依價值屬性分為三大維度，協助藏家做資產配置佈局：人文典藏（人類創作）、大地典藏（自然稀缺）、工業典藏（工藝造物）。",
    "prev": ("品牌短句","../brand/04-slogans.html"),
    "next": ("人文典藏","humanity.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/category.webp" alt="9Turn 九回錦三大分類：人文大地工業" loading="lazy" width="800" height="600"><figcaption>三大分類｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 為什麼要先分三大類？</h2>
<p>九樣資產混在一起看會眼花，拆成三類就清楚：<strong>人文</strong>（人類創作的歷史痕跡）、<strong>大地</strong>（自然原生的稀缺物）、<strong>工業</strong>（經典工藝的造物）。三類的價值來源、風險特性與持有邏輯各不相同，分開看，資產配置才做得對。</p>

<h2>2. 三大分類一覽：各有哪些資產？</h2>
<table>
<colgroup><col style="width:18%"><col style="width:32%"><col style="width:50%"></colgroup>
<thead><tr><th>分類</th><th>資產項目</th><th>核心價值</th></tr></thead>
<tbody>
<tr><td><b>人文典藏</b></td><td>典藏藝術品<br>典藏宅邸／稀有地產<br>古董文玩</td><td>人類創作與歷史痕跡，承載藝術史與文化脈絡。</td></tr>
<tr><td><b>大地典藏</b></td><td>珍稀珠寶<br>經典酒茶<br>頂級原木與珍稀木材</td><td>自然原生稀缺物，仰賴地質、風土與生長週期。</td></tr>
<tr><td><b>工業典藏</b></td><td>經典名錶<br>經典樂器<br>珍稀錢幣與典藏珍郵</td><td>經典工藝造物，重視工藝、聲學、版別與品相。</td></tr>
</tbody>
</table>

<h2>3. 三類之間的配置邏輯，有什麼不同？</h2>
<div class="card-grid">
  <div class="card card-feature"><span class="num">人</span><h3>人文典藏</h3><p>成長性來自文化價值的累積，適合看重藝術與歷史脈絡的藏家。</p></div>
  <div class="card card-feature"><span class="num">地</span><h3>大地典藏</h3><p>稀缺性來自自然供給的限制，天然稀缺、不易複製。</p></div>
  <div class="card card-feature"><span class="num">工</span><h3>工業典藏</h3><p>穩定性來自經典工藝與品牌傳承，適合求穩、求質的藏家。</p></div>
</div>

<h2>4. 三維佈局，為什麼一盤成錦？</h2>
<p>好的資產配置，是把三類都納入考量，讓不同屬性的資產互補。<strong>人文、大地、工藝，三維佈局典藏資產</strong>——這就是九回錦給你的配置骨架。</p>
""",
}

PAGES["category-humanity"] = {
    "out_dir": "category", "file": "humanity.html",
    "title": "人文典藏｜人類創作與歷史痕跡 資產解析",
    "desc": "人文典藏解析：典藏藝術品、典藏宅邸／稀有地產、古董文玩。人類創作與歷史痕跡的三大資產，價值來自文化脈絡與不可複製。",
    "kw": "9Turn,九回錦,人文典藏,典藏藝術品,稀有地產,古董文玩",
    "section": "三大分類",
    "crumb": [("首頁","../index.html"), ("三大分類","../category/index.html"), ("人文典藏","../category/humanity.html")],
    "h1": "人文典藏：為什麼人類創作與歷史痕跡能成資產？",
    "lede": "這一大類，收藏的是「人」留下來的東西——藝術、地產、文玩。價值來自人類的創造力與時代的痕跡。",
    "layout": "2col",
    "sidebar_html": category_side("humanity"),
    "prev": ("三大分類總覽","index.html"),
    "next": ("大地典藏","earth.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/category.webp" alt="9Turn 九回錦人文典藏：人類創作與歷史痕跡" loading="lazy" width="800" height="600"><figcaption>人文典藏｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 什麼是人文典藏？</h2>
<p>人文典藏，指的是<strong>人類創作與歷史痕跡</strong>——由人親手創造、承載藝術史與文化脈絡的資產。它們的價值，很大一部分來自「不可複製」：畫家不會再畫第二張同樣的畫，地段不會再長出一塊同樣的土地。</p>

<h2>2. 人文典藏包含哪三樣？憑什麼進這一類？</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>資產項目</th><th>核心價值</th></tr></thead>
<tbody>
<tr><td><a href="../asset/art.html">典藏藝術品</a></td><td>有完整來源、展覽與出版紀錄的原作，承載藝術史脈絡。</td></tr>
<tr><td><a href="../asset/estate.html">典藏宅邸／稀有地產</a></td><td>地段稀缺、建築具設計或歷史價值、供給難以複製。</td></tr>
<tr><td><a href="../asset/antique.html">古董文玩</a></td><td>傳世有序、鑑定完整的古器物與文房雅藏。</td></tr>
</tbody>
</table>

<h2>3. 人文典藏的判斷重點，看什麼？</h2>
<ul>
  <li><strong>創作脈絡：</strong>藝術品的價值不在視覺好看，而在不可複製的創作脈絡、藝術家定位與完整溯源。</li>
  <li><strong>地段與建築：</strong>地產的價值不在裝潢奢華，而在稀缺地段、建築文化價值與區域供給限制。</li>
  <li><strong>傳世與真偽：</strong>文玩的價值在流傳百年的時代痕跡，須審核真偽、傳世紀錄與保存狀態。</li>
</ul>

<h2>4. 給人文藏家的話：買的是什麼？</h2>
<div class="callout"><div class="ico">人</div><div><strong>人文典藏買的是「人」的證明。</strong>它讓你持有的，不只是資產，更是一段可以被述說的故事。</div></div>
""",
}

PAGES["category-earth"] = {
    "out_dir": "category", "file": "earth.html",
    "title": "大地典藏｜自然原生稀缺物 資產解析",
    "desc": "大地典藏解析：珍稀珠寶、經典酒茶、頂級原木與珍稀木材。自然原生稀缺物，價值來自地質、風土與長期生長。",
    "kw": "9Turn,九回錦,大地典藏,珍稀珠寶,經典酒茶,頂級原木,珍稀木材",
    "section": "三大分類",
    "crumb": [("首頁","../index.html"), ("三大分類","../category/index.html"), ("大地典藏","../category/earth.html")],
    "h1": "大地典藏：為什麼自然原生的東西才算稀缺？",
    "lede": "這一類收藏的是「大地」給的東西——寶石、老酒老茶、珍貴木材。價值來自自然供給的稀缺。",
    "layout": "2col",
    "sidebar_html": category_side("earth"),
    "prev": ("人文典藏","humanity.html"),
    "next": ("工業典藏","industry.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/category.webp" alt="9Turn 九回錦大地典藏：自然原生稀缺物" loading="lazy" width="800" height="600"><figcaption>大地典藏｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 什麼是大地典藏？</h2>
<p>大地典藏，指的是<strong>自然原生的稀缺物</strong>——由地質、風土、時間孕育而生的資產。它們的稀缺，來自大自然「給一次就不給了」的定律。</p>

<h2>2. 大地典藏包含哪三樣？稀缺從哪來？</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>資產項目</th><th>核心價值</th></tr></thead>
<tbody>
<tr><td><a href="../asset/jewelry.html">珍稀珠寶</a></td><td>天然寶石、古董珠寶、大師設計典藏珠寶，附國際鑑定證書。</td></tr>
<tr><td><a href="../asset/wine-tea.html">經典酒茶</a></td><td>頂級陳年酒與典藏老茶，仰賴風土與長期熟成。</td></tr>
<tr><td><a href="../asset/timber.html">頂級原木與珍稀木材</a></td><td>生長週期長、原生資源枯竭的珍貴大料，來源合法可追溯。</td></tr>
</tbody>
</table>

<h2>3. 大地典藏的判斷重點，看什麼？</h2>
<ul>
  <li><strong>等級與證書：</strong>珠寶聚焦寶石等級、產地證書、設計師背景與完整溯源。</li>
  <li><strong>陳年潛力：</strong>能成為資產的酒茶不只是好喝，須具備陳年潛力、名廠與完整倉儲紀錄。</li>
  <li><strong>來源與大料：</strong>木材如海南黃花梨、小葉紫檀等生長緩慢、大料難得，審查來源合法性與保存狀態。</li>
</ul>

<h2>4. 給大地藏家的話：買的是什麼？</h2>
<div class="callout"><div class="ico">地</div><div><strong>大地典藏買的是「自然給的稀缺」。</strong>它天然稀缺、不易複製，是穿越週期很穩的底層資產。</div></div>
""",
}

PAGES["category-industry"] = {
    "out_dir": "category", "file": "industry.html",
    "title": "工業典藏｜經典工藝造物 資產解析",
    "desc": "工業典藏解析：經典名錶、經典樂器、珍稀錢幣與典藏珍郵。經典工藝造物，價值來自工藝、聲學、版別與品相。",
    "kw": "9Turn,九回錦,工業典藏,經典名錶,經典樂器,珍稀錢幣,典藏珍郵",
    "section": "三大分類",
    "crumb": [("首頁","../index.html"), ("三大分類","../category/index.html"), ("工業典藏","../category/industry.html")],
    "h1": "工業典藏：為什麼經典工藝造物能穿越週期？",
    "lede": "這一類收藏的是「工藝」做出來的東西——名錶、樂器、錢幣珍郵。價值來自人類工藝的極致。",
    "layout": "2col",
    "sidebar_html": category_side("industry"),
    "prev": ("大地典藏","earth.html"),
    "next": ("九大資產總覽","../asset/index.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/category.webp" alt="9Turn 九回錦工業典藏：經典工藝造物" loading="lazy" width="800" height="600"><figcaption>工業典藏｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 什麼是工業典藏？</h2>
<p>工業典藏，指的是<strong>經典工藝的造物</strong>——由人類工藝極致打造、經得起時間檢驗的資產。它介於「人」與「地」之間：靠人的手藝，也靠材料與聲學的本質。</p>

<h2>2. 工業典藏包含哪三樣？憑什麼進這一類？</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>資產項目</th><th>核心價值</th></tr></thead>
<tbody>
<tr><td><a href="../asset/watch.html">經典名錶</a></td><td>限量、全套保卡與維修紀錄的經典機械腕錶。</td></tr>
<tr><td><a href="../asset/instrument.html">經典樂器</a></td><td>名家手工製作的提琴、古典吉他，重視聲學品質與來源。</td></tr>
<tr><td><a href="../asset/coin-stamp.html">珍稀錢幣與典藏珍郵</a></td><td>古錢、珍稀金銀幣、初版罕見郵票，重視版別與品相。</td></tr>
</tbody>
</table>

<h2>3. 工業典藏的判斷重點，看什麼？</h2>
<ul>
  <li><strong>原始狀態：</strong>名錶看重原始狀態、全套保卡、出廠與維修紀錄，避開短期炒作熱款。</li>
  <li><strong>製琴師與聲學：</strong>樂器重視製琴師背景、聲學品質、完整來源與保存狀態；量產工廠樂器不列入。</li>
  <li><strong>版別與評級：</strong>錢幣珍郵重視版別、品相、來源與權威評級；普通流通幣不納入。</li>
</ul>

<h2>4. 給工業藏家的話：買的是什麼？</h2>
<div class="callout"><div class="ico">工</div><div><strong>工業典藏買的是「工藝的極致」。</strong>它靠手藝與本質立足，適合求穩、求質的藏家。</div></div>
""",
}

# ============================================================
# 九大資產
# ============================================================
def asset_side(current):
    groups = {
        "humanity": [("典藏藝術品","art.html","art"),("典藏宅邸／稀有地產","estate.html","estate"),("古董文玩","antique.html","antique")],
        "earth": [("珍稀珠寶","jewelry.html","jewelry"),("經典酒茶","wine-tea.html","wine-tea"),("頂級原木","timber.html","timber")],
        "industry": [("經典名錶","watch.html","watch"),("經典樂器","instrument.html","instrument"),("珍稀錢幣與珍郵","coin-stamp.html","coin-stamp")],
    }
    box = [('<div class="box"><img class="box-img" src="assets/img/asset.webp" alt="九大資產" loading="lazy"><h4>九大資產</h4><ul>'+
            '<li><a href="index.html">九大資產總覽</a></li></ul></div>')]
    for k, items in groups.items():
        lis = ""
        for t,u,key in items:
            cls = "active" if key == current else ""
            lis += f'<li><a class="{cls}" href="{u}">{t}</a></li>'
        box.append(f'<div class="box"><h4>{"人文" if k=="humanity" else "大地" if k=="earth" else "工業"}典藏</h4><ul>{lis}</ul></div>')
    return "".join(box)

PAGES["asset-index"] = {
    "out_dir": "asset", "file": "index.html",
    "title": "九大資產總覽｜9Turn 九回錦 硬資產清單",
    "desc": "9Turn 九回錦九大資產總覽：典藏藝術品、稀有地產、古董文玩、珍稀珠寶、經典酒茶、頂級原木、經典名錶、經典樂器、珍稀錢幣與珍郵。",
    "kw": "9Turn,九回錦,九大資產,典藏藝術品,珍稀珠寶,經典名錶,硬資產",
    "section": "九大資產",
    "crumb": [("首頁","../index.html"), ("九大資產","../asset/index.html")],
    "h1": "九大資產：九樣珍品，憑什麼都能進典藏名單？",
    "lede": "把九大典藏資產一次攤開：每一樣都講清「它值在哪、怎麼看、為什麼值得長久持有」。",
    "prev": ("工業典藏","../category/industry.html"),
    "next": ("典藏藝術品","art.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/asset.webp" alt="9Turn 九回錦九大資產總覽" loading="lazy" width="800" height="600"><figcaption>九大資產總覽｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 九大資產是哪九樣？憑什麼都算資產？</h2>
<div class="card-grid">
  <div class="card"><img src="assets/img/art.webp" alt="典藏藝術品滿版配圖" loading="lazy"><span class="num">01</span><h3>典藏藝術品</h3><p>來源、展覽與出版紀錄完整的原作。</p><a class="card-link" href="art.html">→</a></div>
  <div class="card"><img src="assets/img/estate.webp" alt="典藏宅邸稀有地產滿版配圖" loading="lazy"><span class="num">02</span><h3>典藏宅邸／稀有地產</h3><p>地段稀缺、供給難複製的地產。</p><a class="card-link" href="estate.html">→</a></div>
  <div class="card"><img src="assets/img/antique.webp" alt="古董文玩滿版配圖" loading="lazy"><span class="num">03</span><h3>古董文玩</h3><p>傳世有序、鑑定完整的古器物。</p><a class="card-link" href="antique.html">→</a></div>
  <div class="card"><img src="assets/img/jewelry.webp" alt="珍稀珠寶滿版配圖" loading="lazy"><span class="num">04</span><h3>珍稀珠寶</h3><p>天然寶石、古董珠寶、大師設計。</p><a class="card-link" href="jewelry.html">→</a></div>
  <div class="card"><img src="assets/img/wine-tea.webp" alt="經典酒茶滿版配圖" loading="lazy"><span class="num">05</span><h3>經典酒茶</h3><p>頂級陳年酒與典藏老茶。</p><a class="card-link" href="wine-tea.html">→</a></div>
  <div class="card"><img src="assets/img/timber.webp" alt="頂級原木滿版配圖" loading="lazy"><span class="num">06</span><h3>頂級原木</h3><p>生長週期長、資源枯竭的珍貴大料。</p><a class="card-link" href="timber.html">→</a></div>
  <div class="card"><img src="assets/img/watch.webp" alt="經典名錶滿版配圖" loading="lazy"><span class="num">07</span><h3>經典名錶</h3><p>限量、全套保卡的機械腕錶。</p><a class="card-link" href="watch.html">→</a></div>
  <div class="card"><img src="assets/img/instrument.webp" alt="經典樂器滿版配圖" loading="lazy"><span class="num">08</span><h3>經典樂器</h3><p>名家手工製作的聲學傑作。</p><a class="card-link" href="instrument.html">→</a></div>
  <div class="card"><img src="assets/img/coin.webp" alt="珍稀錢幣與珍郵滿版配圖" loading="lazy"><span class="num">09</span><h3>珍稀錢幣與珍郵</h3><p>古錢、珍稀金銀幣、初版郵票。</p><a class="card-link" href="coin-stamp.html">→</a></div>
</div>

<h2>2. 九樣資產的共同守則是什麼？</h2>
<p>無論是哪一樣，都必須通過<strong>四大準則</strong>審核：稀缺性、底層價值、完整溯源、長期典藏屬性。不符合的，就算當下行情火熱，也不納入。<a href="../criteria/index.html">看完整審核邏輯 →</a></p>

<h2>3. 三大分類 × 九大資產，怎麼對照？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>分類</th><th>資產</th></tr></thead>
<tbody>
<tr><td>人文典藏</td><td>典藏藝術品、典藏宅邸／稀有地產、古董文玩</td></tr>
<tr><td>大地典藏</td><td>珍稀珠寶、經典酒茶、頂級原木與珍稀木材</td></tr>
<tr><td>工業典藏</td><td>經典名錶、經典樂器、珍稀錢幣與典藏珍郵</td></tr>
</tbody>
</table>
""",
}

ASSET_ALT = {
    "art":"經典油畫原作典藏","estate":"古典莊園稀有地產典藏","antique":"清代青花瓷瓶古董文玩典藏",
    "jewelry":"祖母綠鑽石項鍊珍稀珠寶典藏","wine-tea":"陳年茶餅與紫砂茶器經典酒茶典藏",
    "timber":"頂級原木年輪珍稀木材典藏","watch":"經典陀飛輪機械腕錶典藏",
    "instrument":"名家手工小提琴經典樂器典藏","coin":"珍稀古金幣與銀幣錢幣郵票典藏",
}

def asset_page(slug, title, h1, lede, desc, kw, num, crumb, prev, next, body):
    fname = slug.split("-", 1)[1] + ".html"
    key = slug.split("-", 1)[1]
    img_key = {"coin-stamp": "coin"}.get(key, key)
    alt = ASSET_ALT.get(key, h1)
    fig = (f'<figure class="asset-fig"><img src="assets/img/{img_key}.webp" '
           f'alt="{alt}" loading="lazy" width="800" height="600">'
           f'<figcaption>{alt}｜9Turn 九回錦典藏研究</figcaption></figure>')
    body = fig + "\n" + body
    deep_dir = fname[:-5]  # art.html -> "art"，連到 asset/art/index.html
    body = body + (
        '\n<h2>5. 深度專區：22 篇知識文章一次讀透</h2>\n'
        '<p>主題概覽看完了，想更深入？9Turn 為每樣資產精選 22 篇深度知識文章，從鑑定、市場、保存到傳承，'
        '帶你建立完整的典藏知識框架。</p>\n'
        '<p style="text-align:center;margin-top:18px">'
        f'<a class="btn btn-gold" href="{deep_dir}/index.html">進入「{h1.split("：")[0]}」深度專區 →</a></p>'
    )
    PAGES[slug] = {
        "out_dir":"asset","file":fname,"title":title,"desc":desc,"kw":kw,
        "section":"九大資產",
        "crumb":[("首頁","../index.html"),("九大資產","../asset/index.html"),(h1,"../asset/"+fname)],
        "h1":h1,"lede":lede,"layout":"2col","sidebar_html":asset_side(slug.split("-")[-1]),
        "prev":prev,"next":next,"body":body,
    }

asset_page("asset-art","典藏藝術品｜不可複製的創作脈絡","典藏藝術品：為什麼買的是不可複製的創作脈絡？",
"藝術的價值不在視覺好看，而在不可複製的創作脈絡、藝術家定位與完整溯源。9Turn 僅收錄溯源完整的原作。",
"9Turn 九回錦典藏藝術品解析：藝術價值在創作脈絡、藝術家定位與完整溯源。如何判斷一件原作是否值得長期典藏。","典藏藝術品,原作,藝術家,溯源,9Turn",
"01","（首頁 → 九大資產）",
("九大資產總覽","index.html"),("典藏宅邸／稀有地產","estate.html"),
"""
<h2>1. 藝術品的價值，為什麼不在「好看」？</h2>
<p>很多人以為畫得好看就是好藝術品。其實藝術品的價值核心在<strong>不可複製的創作脈絡</strong>——這件作品在藝術史中的位置、藝術家的定位、以及它背後完整的來源故事。</p>

<h2>2. 我們審什麼？四件事一次看</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>審查重點</th><th>看什麼</th></tr></thead>
<tbody>
<tr><td>來源</td><td>作品從誰手上來、歷經哪些手，來源清楚。</td></tr>
<tr><td>展覽紀錄</td><td>有無重要展覽經歷，證明其被藝術圈認可。</td></tr>
<tr><td>出版資料</td><td>有無畫冊、圖錄、權威出版收錄。</td></tr>
<tr><td>保存狀態</td><td>品相完整程度，影響長期價值。</td></tr>
</tbody>
</table>

<h2>3. 為什麼藝術品值得長久持有？</h2>
<div class="callout"><div class="ico">◎</div><div><strong>畫家不會再畫第二張同樣的畫。</strong>稀缺來自不可複製——這就是藝術品穿越市場週期的底層邏輯。</div></div>
<p>市場熱潮會退，但一件真正承載藝術史脈絡的原作，它的文化價值會隨時間累積，而不是隨炒作消退。據公開報導，<strong>張大千</strong>《桃源圖》於 2016 年香港拍賣以約 2.7 億港元成交，頂級華人原作的身價由此可見。</p>

<h2>4. 給藝術藏家的一句話：先問哪三題？</h2>
<p>買藝術品前，先問三句：<strong>這件作品的來源完整嗎？它在藝術史裡有位置嗎？它是藝術家重要階段的代表嗎？</strong>三題都過，才值得典藏。</p>
""")

asset_page("asset-estate","典藏宅邸｜稀有地產 地段與建築的雙重稀缺","典藏宅邸／稀有地產：為什麼地段與建築是雙重稀缺？",
"一間房子能否成為資產，不在裝潢奢華，而在稀缺地段、建築文化價值、區域供給限制與長期基本面。",
"9Turn 九回錦典藏宅邸／稀有地產解析：地段稀缺、建築文化價值、供給限制與長期基本面如何決定地產的典藏價值。","稀有地產,典藏宅邸,地段,建築,9Turn",
"02","（首頁 → 九大資產）",
("典藏藝術品","art.html"),("古董文玩","antique.html"),
"""
<h2>1. 地產也能「典藏」？憑什麼？</h2>
<p>當然。但不是每間房子都算資產——<strong>一間房子能否成為資產，不在裝潢奢華，而在稀缺地段、建築文化價值、區域供給限制與長期基本面。</strong></p>

<h2>2. 四把尺量一間地產，怎麼量？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>尺</th><th>衡量什麼</th></tr></thead>
<tbody>
<tr><td>地段邏輯</td><td>所在區域是否稀缺、發展基本面是否穩健。</td></tr>
<tr><td>建築價值</td><td>有無設計或歷史價值，能否成為文化資產。</td></tr>
<tr><td>供給限制</td><td>區域供給是否受限、難以複製新供給。</td></tr>
<tr><td>持有風險</td><td>流通性與長期持有風險是否可控。</td></tr>
</tbody>
</table>

<h2>3. 為什麼稀缺地產能穿越週期？</h2>
<div class="callout"><div class="ico">地</div><div><strong>土地是稀缺的，地段是複製不來的。</strong>好地段只會越來越少，這就是地產的底層價值。</div></div>

<h2>4. 給地產藏家的一句話：看什麼？</h2>
<p>看地產不要被裝潢迷惑，要看<strong>這塊地、這棟樓，十年後還值不值、二十年后還能不能傳下去。</strong></p>
""")

asset_page("asset-antique","古董文玩｜傳世百年的時代痕跡","古董文玩：為什麼流傳百年的時代痕跡才算數？",
"古董文玩是流傳百年的時代痕跡。審核真偽、出土或傳世紀錄、修復歷史與保存狀態，淘汰仿品與後期量產仿古商品。",
"9Turn 九回錦古董文玩解析：傳世有序、鑑定完整的古器物與文房雅藏。如何分辨真品與仿品、看懂傳世紀錄。","古董文玩,古器物,文房,鑑定,仿品,9Turn",
"03","（首頁 → 九大資產）",
("典藏宅邸／稀有地產","estate.html"),("珍稀珠寶","jewelry.html"),
"""
<h2>1. 文玩收藏的，為什麼是「時間」？</h2>
<p><strong>骨董</strong>文玩，收藏的不只是器物，更是<strong>流傳百年的時代痕跡</strong>。一件傳世有序的器物，身上帶著歷代藏家的故事，這是新做仿品永遠模仿不來的。</p>

<h2>2. 我們怎麼把關真偽？四件事</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>把關重點</th><th>看什麼</th></tr></thead>
<tbody>
<tr><td>真偽鑑定</td><td>由專業鑑定把關，排除仿品與後期量產仿古商品。</td></tr>
<tr><td>傳世紀錄</td><td>審核出土或傳世的來源紀錄，來源清楚。</td></tr>
<tr><td>修復歷史</td><td>了解歷經哪些修復，影響品相與價值。</td></tr>
<tr><td>保存狀態</td><td>檢查現有保存情況，評估長期持有。</td></tr>
</tbody>
</table>

<h2>3. 為什麼仿品進不了名單？</h2>
<div class="callout"><div class="ico">鑑</div><div><strong>仿品再漂亮，也只是「仿」。</strong>它沒有時代痕跡、沒有傳世脈絡，也就沒有穿越週期的底層價值。</div></div>
<p>據傳，二戰前後荷蘭名畫偽造者<strong>范米格倫（Han van Meegeren）</strong>偽造的維梅爾畫作一度瞞過專家，但最終因畫作科學鑑定露出破綻——這正是為什麼我們把<strong>鑑定證書</strong>與傳世脈絡看得比什麼都重。</p>

<h2>4. 給文玩藏家的一句話：先問什麼？</h2>
<p>收文玩，先問<strong>來源與傳世</strong>，再談美不美。真偽過不了關，一切免談。</p>
""")

asset_page("asset-jewelry","珍稀珠寶｜寶石等級與國際證書","珍稀珠寶：為什麼天然寶石、古董珠寶才是資產？",
"流行飾品會退燒，但高品質天然寶石、古董珠寶與大師典藏珠寶的稀缺性固定不減。聚焦寶石等級、產地證書、設計師背景與完整溯源。",
"9Turn 九回錦珍稀珠寶解析：寶石等級、產地證書、設計師背景與完整溯源，為什麼天然寶石是穿越週期的硬資產。","珍稀珠寶,天然寶石,古董珠寶,鑑定證書,9Turn",
"04","（首頁 → 九大資產）",
("古董文玩","antique.html"),("經典酒茶","wine-tea.html"),
"""
<h2>1. 珠寶的「資產」與「飾品」，差在哪？</h2>
<p>戴著好看的流行飾品會退燒，但<strong>高品質天然寶石、古董珠寶與大師典藏珠寶的稀缺性，固定不減。</strong>差別就在於：前者是消費，後者是資產。</p>

<h2>2. 我們看哪四件事？</h2>
<table>
<colgroup><col style="width:28%"><col style="width:72%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>寶石等級</td><td>克拉、顏色、淨度、切工——等級越高越稀缺。</td></tr>
<tr><td>產地證書</td><td><strong>GIA 證書</strong>等國際鑑定證書確認天然來源與產地。</td></tr>
<tr><td>設計師背景</td><td>大師設計作品，工藝與名號加持價值。</td></tr>
<tr><td>完整溯源</td><td>來源清楚，可追溯。</td></tr>
</tbody>
</table>

<h2>3. 為什麼天然寶石是硬資產？</h2>
<div class="callout"><div class="ico">寶</div><div><strong>天然寶石挖一顆少一顆。</strong>地質給的稀缺，是市場永遠炒作不來的底層價值。</div></div>

<h2>4. 給珠寶藏家的一句話：先要什麼？</h2>
<p>買珠寶前，先要<strong>國際鑑定證書</strong>，再看設計與溯源。證書是身分證，沒有它再美也難當資產。</p>
""")

asset_page("asset-wine-tea","經典酒茶｜風土與長期熟成的資產","經典酒茶：為什麼風土與長期熟成能讓酒茶成資產？",
"能成為資產的酒茶不只是好喝，須具備陳年潛力、名廠與完整倉儲紀錄。嚴審產地、年份、原料等級、包裝與品相。",
"9Turn 九回錦經典酒茶解析：陳年潛力、名廠、倉儲紀錄、風土與熟成。為什麼老酒老茶是能放越值的硬資產。","經典酒茶,陳年老酒,典藏老茶,風土,熟成,9Turn",
"05","（首頁 → 九大資產）",
("珍稀珠寶","jewelry.html"),("頂級原木","timber.html"),
"""
<h2>1. 酒茶不是「喝的」，為什麼是「存的」？</h2>
<p>日常喝的酒茶是消費，但<strong>能成為資產的酒茶不只是好喝，須具備陳年潛力、名廠與完整倉儲紀錄。</strong>它是少數「越放越值」的資產。</p>

<h2>2. 我們審什麼？四件事</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>審查重點</th><th>看什麼</th></tr></thead>
<tbody>
<tr><td>產地</td><td>風土決定品質基底，名產區更具稀缺。</td></tr>
<tr><td>年份與原料等級</td><td>好年份、好原料才有陳年潛力。</td></tr>
<tr><td>名廠</td><td>名廠出品，具品牌與工藝背書。</td></tr>
<tr><td>倉儲紀錄</td><td>存放條件完整，品相才保得住。</td></tr>
</tbody>
</table>

<h2>3. 為什麼老酒老茶能穿越週期？</h2>
<div class="callout"><div class="ico">藏</div><div><strong>時間是酒茶的釀造者。</strong>每多放一年，稀缺與品質就多一分——這是歲月給的資產。</div></div>

<h2>4. 給酒茶藏家的一句話：先問什麼？</h2>
<p>買老酒老茶，先問<strong>倉儲紀錄</strong>。存不好，再好的酒茶也會「壞掉變消費品」。</p>
""")

asset_page("asset-timber","頂級原木｜珍稀木材 來源合法可追溯","頂級原木與珍稀木材：為什麼生長週期長的大料才值錢？",
"海南黃花梨、小葉紫檀、老紅木等生長緩慢、大料難得的珍貴材料。審查來源合法性、木材種類、紋理與保存狀態。",
"9Turn 九回錦頂級原木與珍稀木材解析：海南黃花梨、小葉紫檀、老紅木的稀缺價值與來源合法性審查。","頂級原木,海南黃花梨,小葉紫檀,老紅木,珍稀木材,9Turn",
"06","（首頁 → 九大資產）",
("經典酒茶","wine-tea.html"),("經典名錶","watch.html"),
"""
<h2>1. 木頭也能是硬資產？憑什麼？</h2>
<p>不是所有木頭都值錢，只有<strong>生長週期長、原生資源枯竭的珍貴大料</strong>才夠格。像海南黃花梨、小葉紫檀、老紅木，動輒長數十年上百年，大料更是難得。</p>

<h2>2. 我們審什麼？四件事</h2>
<table>
<colgroup><col style="width:28%"><col style="width:72%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>來源合法性</td><td>來源合法、可追溯，杜絕盜伐。</td></tr>
<tr><td>木材種類</td><td>是否為珍稀樹種、是否屬原生稀缺。</td></tr>
<tr><td>紋理</td><td>紋理美感與稀有度。</td></tr>
<tr><td>保存狀態</td><td>有無開裂、蟲蛀，影響長期價值。</td></tr>
</tbody>
</table>

<h2>3. 為什麼珍稀木材能穿越週期？</h2>
<div class="callout"><div class="ico">木</div><div><strong>樹要長一百年，砍掉只要一天。</strong>原生資源枯竭、無法速生複製——這就是木頭的底層稀缺。</div></div>

<h2>4. 給木材藏家的一句話：底線是什麼？</h2>
<p>收珍稀木材，<strong>來源合法</strong>是底線。來源不清的再漂亮也不要碰。</p>
""")

asset_page("asset-watch","經典名錶｜限量與完整保卡的機械經典","經典名錶：為什麼只有少數經典限量款能隨時間增值？",
"多數腕錶購入即貶值，只有少數經典限量款隨時間累積價值。看重原始狀態、全套保卡、出廠與維修紀錄，避開短期炒作熱款。",
"9Turn 九回錦經典名錶解析：限量款、全套保卡、原始狀態與維修紀錄。為什麼多數腕錶貶值、少數經典反而增值。","經典名錶,限量腕錶,機械錶,保卡,9Turn",
"07","（首頁 → 九大資產）",
("頂級原木","timber.html"),("經典樂器","instrument.html"),
"""
<h2>1. 腕錶的真相：為什麼多數買來就貶值？</h2>
<p>先講個殘酷事實：<strong>多數腕錶購入即貶值。</strong>只有少數經典限量款，能隨時間累積價值。所以選錶當資產，要的不是「熱門」，而是「經典」。</p>

<h2>2. 我們看什麼？四件事</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>原始狀態</td><td>是否保持出廠原貌，未經亂改。</td></tr>
<tr><td>全套保卡</td><td>配件、保卡齊全，是價值的證明。</td></tr>
<tr><td>出廠與維修紀錄</td><td>歷程清楚，可信度高。</td></tr>
<tr><td>避開炒作熱款</td><td>短期被炒高的熱款，風險大。</td></tr>
</tbody>
</table>

<h2>3. 為什麼經典名錶能穿越週期？</h2>
<div class="callout"><div class="ico">錶</div><div><strong>經典不會退流行，限量不會再增產。</strong>機械工藝的極致＋稀缺的發行量，是它增值的底層邏輯。</div></div>
<p><strong>陀飛輪</strong>等複雜機械功能是高級腕錶的工藝指標；據公開報導，頂級獨立製錶品牌的限量款在<strong>蘇富比</strong>、<strong>佳士得</strong>等拍賣會上常有高出原購入價的成交紀錄。</p>

<h2>4. 給名錶藏家的一句話：先問什麼？</h2>
<p>買名錶當資產，先問<strong>是不是經典限量、保卡紀錄是否完整</strong>，別被一時熱度牽著走。</p>
""")

asset_page("asset-instrument","經典樂器｜名家手工製作的聲學傑作","經典樂器：為什麼名家手工製作的聲學傑作才算數？",
"手工頂級提琴、古典吉他等名家製作樂器，重視製琴師背景、聲學品質、完整來源與保存狀態；量產工廠樂器不列入典藏。",
"9Turn 九回錦經典樂器解析：名家手工提琴、古典吉他的製琴師背景、聲學品質與完整來源。","經典樂器,手工提琴,古典吉他,製琴師,聲學,9Turn",
"08","（首頁 → 九大資產）",
("經典名錶","watch.html"),("珍稀錢幣與珍郵","coin-stamp.html"),
"""
<h2>1. 樂器不只是「樂器」，為什麼？</h2>
<p>對藏家來說，<strong>手工頂級提琴、古典吉他等名家製作樂器</strong>，是兼具聲學品質與工藝傳承的硬資產。量產工廠樂器，不列入典藏範圍。</p>

<h2>2. 我們看什麼？四件事</h2>
<table>
<colgroup><col style="width:28%"><col style="width:72%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>製琴師背景</td><td>名家手作，工藝與名號加持。</td></tr>
<tr><td>聲學品質</td><td>聲音表現是否頂尖，是核心價值。</td></tr>
<tr><td>完整來源</td><td>來源清楚，可追溯。</td></tr>
<tr><td>保存狀態</td><td>琴況是否良好，影響價值。</td></tr>
</tbody>
</table>

<h2>3. 為什麼名家樂器能穿越週期？</h2>
<div class="callout"><div class="ico">音</div><div><strong>琴聲會老，反而更醇。</strong>名家手作的聲學傑作，量產永遠模仿不來。</div></div>
<p>據公開報導，<strong>斯特拉迪瓦里（Stradivari）</strong>與<strong>瓜奈里（Guarneri）</strong>時代的義大利名琴，在國際拍賣會上身價動輒數百萬美元，可見名家手工樂器的稀缺價值。</p>

<h2>4. 給樂器藏家的一句話：先問什麼？</h2>
<p>收樂器，先問<strong>製琴師是誰、聲學品質如何、來源是否完整</strong>。量產貨再貴，也成不了典藏。</p>
""")

asset_page("asset-coin-stamp","珍稀錢幣與典藏珍郵｜版別與品相的雙重講究","珍稀錢幣與典藏珍郵：為什麼版別與品相決定身價？",
"古錢、近代珍稀金銀幣、初版罕見郵票，重視版別、品相、來源與權威評級；普通流通幣與一般紀念郵票不納入。",
"9Turn 九回錦珍稀錢幣與典藏珍郵解析：古錢、珍稀金銀幣、初版郵票的版別、品相與權威評級。","珍稀錢幣,古錢,金銀幣,典藏珍郵,初版郵票,9Turn",
"09","（首頁 → 九大資產）",
("經典樂器","instrument.html"),("四大準則總覽","../criteria/index.html"),
"""
<h2>1. 錢幣珍郵：小物件裡為什麼有大學問？</h2>
<p>一枚古錢、一張初版郵票，看起來小，其實是<strong>版別與品相的雙重講究</strong>。真正的珍稀品，身價可以高得嚇人。</p>

<h2>2. 我們看什麼？四件事</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>版別</td><td>是否為稀有版別、初版罕見品。</td></tr>
<tr><td>品相</td><td>保存狀態、完整度，直接影響價值。</td></tr>
<tr><td>來源</td><td>來源清楚，可追溯。</td></tr>
<tr><td>權威評級</td><td>有無權威機構評級背書。</td></tr>
</tbody>
</table>

<h2>3. 普通品為什麼不算資產？</h2>
<div class="callout"><div class="ico">評</div><div><strong>普通流通幣與一般紀念郵票不納入。</strong>要的是珍稀版別、初版罕見——量多就不值錢。</div></div>
<p>據公開報導，英屬蓋普那「紅色一分錢」等傳奇珍稀郵票，歷年拍賣身價動輒百萬美元級，可見版別與品相的關鍵性。</p>

<h2>4. 給錢幣珍郵藏家的一句話：先問哪三件事？</h2>
<p>收錢幣珍郵，先問<strong>版別、品相、評級</strong>三件事。普通品再漂亮，也只是收藏，不是資產。</p>
""")

# ============================================================
# 四大篩選準則
# ============================================================
def criteria_side(current):
    items = [("四大準則總覽","index.html","index"),
             ("稀缺性","scarcity.html","scarcity"),
             ("底層價值","value.html","value"),
             ("完整溯源","provenance.html","provenance"),
             ("長期典藏屬性","longterm.html","longterm")]
    lis = ""
    for t,u,k in items:
        cls = "active" if k == current else ""
        lis += f'<li><a class="{cls}" href="{u}">{t}</a></li>'
    return '<div class="box"><img class="box-img" src="assets/img/criteria.webp" alt="四大準則" loading="lazy"><h4>四大準則</h4><ul>' + lis + "</ul></div>"

PAGES["criteria-index"] = {
    "out_dir": "criteria", "file": "index.html",
    "title": "價值篩選四大準則｜9Turn 九回錦 審核邏輯",
    "desc": "9Turn 九回錦價值篩選四大準則：稀缺性、底層價值、完整溯源、長期典藏屬性。任何標的都須通過這四道審核才進典藏名單。",
    "kw": "9Turn,九回錦,四大準則,稀缺性,底層價值,完整溯源,長期典藏",
    "section": "四大準則",
    "crumb": [("首頁","../index.html"), ("四大準則","../criteria/index.html")],
    "h1": "價值篩選四大準則：為什麼過得了這四關才算資產？",
    "lede": "任何標的都必須通過以下四道審核，才會進入 9Turn 典藏名單；就算當下行情火熱，不符合者一律不納入。",
    "prev": ("珍稀錢幣與珍郵","../asset/coin-stamp.html"),
    "next": ("稀缺性","scarcity.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/criteria.webp" alt="9Turn 九回錦價值篩選四大準則" loading="lazy" width="800" height="600"><figcaption>四大準則總覽｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 為什麼需要審核？</h2>
<p>市場上貴的東西很多，但<strong>貴不等於資產</strong>。為了不讓藏家被一時熱度誤導，9Turn 訂下四道硬關卡，過不了就進不了典藏名單。</p>

<h2>2. 四大準則，各管什麼？</h2>
<table>
<colgroup><col style="width:20%"><col style="width:30%"><col style="width:50%"></colgroup>
<thead><tr><th>關卡</th><th>一句話</th><th>過不了的下場</th></tr></thead>
<tbody>
<tr><td><strong>稀缺性</strong></td><td>供給有限，無法量產複製。</td><td>能量產的就不是資產，只是商品。</td></tr>
<tr><td><strong>底層價值</strong></td><td>美學、歷史、工藝、材料或土地本質。</td><td>熱潮一退，價值跟著蒸發。</td></tr>
<tr><td><strong>完整溯源</strong></td><td>來源清晰，文件脈絡齊全。</td><td>像沒有戶口的房子，轉手就出問題。</td></tr>
<tr><td><strong>長期典藏</strong></td><td>適合持有、傳承，有流通基礎。</td><td>買來放不住、傳不下去，就只是消費。</td></tr>
</tbody>
</table>

<h2>3. 四關缺一不可，為什麼？</h2>
<p>這四道不是「四選一」，而是<strong>四道全過</strong>。就算某樣東西當下行情火熱，只要有一關不過，9Turn 一律不納入。這是我們對藏家的責任。</p>

<h2>4. 一句話記住：四個字是什麼？</h2>
<div class="callout"><div class="ico">關</div><div><strong>稀缺、有底、溯源、能傳。</strong>四個字，就是九回錦的選物標準。</div></div>
""",
}

PAGES["criteria-scarcity"] = {
    "out_dir": "criteria", "file": "scarcity.html",
    "title": "稀缺性準則｜供給有限 無法量產複製",
    "desc": "9Turn 九回錦稀缺性準則解析：供給有限、無法量產複製才是真稀缺。看懂稀缺性為何是硬資產的第一道門檻。",
    "kw": "9Turn,九回錦,稀缺性,供給有限,無法複製,硬資產",
    "section": "四大準則",
    "crumb": [("首頁","../index.html"), ("四大準則","../criteria/index.html"), ("稀缺性","../criteria/scarcity.html")],
    "h1": "準則一：稀缺性——為什麼供給有限、無法複製才算資產？",
    "lede": "第一道關卡。沒有稀缺，一切都是空談。",
    "layout": "2col",
    "sidebar_html": criteria_side("scarcity"),
    "prev": ("四大準則總覽","index.html"),
    "next": ("底層價值","value.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/criteria.webp" alt="四大準則：稀缺性把關第一關" loading="lazy" width="800" height="600"><figcaption>稀缺性準則｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 稀缺性是什麼？白話一次講懂</h2>
<p>稀缺性，白話講就是<strong>「這東西要嘛天生不多，要嘛做不出第二份」</strong>。供給有限、無法量產複製，這是硬資產的第一道門檻。</p>

<h2>2. 稀缺從哪來？三種來源一次看</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>來源</th><th>例子</th></tr></thead>
<tbody>
<tr><td>自然稀缺</td><td>天然寶石、珍稀木材——地質與生長給的，挖一顆少一顆。</td></tr>
<tr><td>創作稀缺</td><td>藝術原作、名家樂器——作者不會再做第二件。</td></tr>
<tr><td>供給受限</td><td>稀有地產、限量名錶——供給被鎖死，無法增產。</td></tr>
</tbody>
</table>

<h2>3. 為什麼稀缺是四關裡的第一關？</h2>
<div class="callout"><div class="ico">壹</div><div><strong>能量產的，永遠輪不到你當主角。</strong>稀缺是價值的起點——不稀缺，後面三關都白談。</div></div>

<h2>4. 一句話記住：先問它能不能被複製</h2>
<p>看到一樣東西，先問：<strong>它能被複製嗎？</strong>只要能被大量複製，它就不可能是典藏級資產。</p>
""",
}

PAGES["criteria-value"] = {
    "out_dir": "criteria", "file": "value.html",
    "title": "底層價值準則｜美學 歷史 工藝 材料 土地本質",
    "desc": "9Turn 九回錦底層價值準則解析：美學、歷史、工藝、材料或土地本質價值，不受短期市場熱潮牽制。",
    "kw": "9Turn,九回錦,底層價值,美學價值,歷史價值,工藝價值",
    "section": "四大準則",
    "crumb": [("首頁","../index.html"), ("四大準則","../criteria/index.html"), ("底層價值","../criteria/value.html")],
    "h1": "準則二：底層價值——為什麼不受短期熱潮牽制才值錢？",
    "lede": "第二道關卡。價值必須長在「本質」上，而不是長在「熱度」上。",
    "layout": "2col",
    "sidebar_html": criteria_side("value"),
    "prev": ("稀缺性","scarcity.html"),
    "next": ("完整溯源","provenance.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/criteria.webp" alt="9Turn 九回錦底層價值準則" loading="lazy" width="800" height="600"><figcaption>底層價值準則｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 什麼是底層價值？</h2>
<p>底層價值，指的是<strong>具備美學、歷史、工藝、材料或土地本質的價值</strong>。它不靠市場情緒撐腰，就算炒作退潮，價值依然在。</p>

<h2>2. 五種底層價值，各是什麼？</h2>
<table>
<colgroup><col style="width:22%"><col style="width:78%"></colgroup>
<thead><tr><th>類型</th><th>說明</th></tr></thead>
<tbody>
<tr><td>美學價值</td><td>作品本身的美，經得起時間考驗。</td></tr>
<tr><td>歷史價值</td><td>承載時代與文化的脈絡。</td></tr>
<tr><td>工藝價值</td><td>人類工藝的極致，量產做不來。</td></tr>
<tr><td>材料價值</td><td>天然材料的稀缺與品質。</td></tr>
<tr><td>土地價值</td><td>地段的稀缺與基本面的穩健。</td></tr>
</tbody>
</table>

<h2>3. 熱度與本質，差在哪？</h2>
<div class="callout"><div class="ico">貳</div><div><strong>熱度會散，本質不會。</strong>靠炒作漲上去的，遲早跌回來；長在本質上的，時間站在它那邊。</div></div>

<h2>4. 一句話記住：怎麼判斷有底層價值？</h2>
<p>問自己：<strong>如果明天市場冷掉了，它還值錢嗎？</strong>會，才叫有底層價值。</p>
""",
}

PAGES["criteria-provenance"] = {
    "out_dir": "criteria", "file": "provenance.html",
    "title": "完整溯源準則｜來源清晰 文件脈絡齊全",
    "desc": "9Turn 九回錦完整溯源準則解析：來源清晰、文件脈絡齊全、可追溯。為何溯源是硬資產的通行證。",
    "kw": "9Turn,九回錦,完整溯源,來源,文件,可追溯,通行證",
    "section": "四大準則",
    "crumb": [("首頁","../index.html"), ("四大準則","../criteria/index.html"), ("完整溯源","../criteria/provenance.html")],
    "h1": "準則三：完整溯源——為什麼來源清楚、文件齊全才算通行證？",
    "lede": "第三道關卡。沒有身分證的資產，價值再高也難傳承。",
    "layout": "2col",
    "sidebar_html": criteria_side("provenance"),
    "prev": ("底層價值","value.html"),
    "next": ("長期典藏屬性","longterm.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/criteria.webp" alt="9Turn 九回錦完整溯源準則" loading="lazy" width="800" height="600"><figcaption>完整溯源準則｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 溯源是什麼？白話一次講懂</h2>
<p>完整溯源，指的是<strong>來源清晰、文件脈絡齊全、可追溯</strong>。白話講就是：這東西從哪裡來、經過哪些手、都有文件證明。</p>

<h2>2. 為什麼溯源是通行證？</h2>
<div class="callout"><div class="ico">參</div><div><strong>來源不清，就像沒有戶口的房子。</strong>價值再高，一轉手就出問題，更別說世代傳承。</div></div>

<h2>3. 溯源要看什麼？三樣東西</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>溯源項目</th><th>看什麼</th></tr></thead>
<tbody>
<tr><td>來源紀錄</td><td>從誰手上來、歷經哪些手。</td></tr>
<tr><td>權威文件</td><td><strong>鑑定證書</strong>、出版、評級文件。</td></tr>
<tr><td>傳世脈絡</td><td>有無清楚的流傳歷史。</td></tr>
</tbody>
</table>

<h2>4. 一句話記住：怎麼判斷溯源夠不夠？</h2>
<p>問自己：<strong>這東西的來龍去脈，我說得清楚嗎？</strong>說不清，就不要當資產買。</p>
""",
}

PAGES["criteria-longterm"] = {
    "out_dir": "criteria", "file": "longterm.html",
    "title": "長期典藏屬性準則｜適合持有與傳承",
    "desc": "9Turn 九回錦長期典藏屬性準則解析：適合持有、傳承、具備穩定長期流通基礎。看懂資產與消費的分界。",
    "kw": "9Turn,九回錦,長期典藏,世代傳承,長期持有,流通基礎",
    "section": "四大準則",
    "crumb": [("首頁","../index.html"), ("四大準則","../criteria/index.html"), ("長期典藏屬性","../criteria/longterm.html")],
    "h1": "準則四：長期典藏屬性——為什麼適合持有與傳承才算資產？",
    "lede": "第四道關卡。不能傳下去的，就還稱不上資產。",
    "layout": "2col",
    "sidebar_html": criteria_side("longterm"),
    "prev": ("完整溯源","provenance.html"),
    "next": ("全流程服務","../service/index.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/criteria.webp" alt="9Turn 九回錦長期典藏屬性準則" loading="lazy" width="800" height="600"><figcaption>長期典藏屬性準則｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 什麼是長期典藏屬性？</h2>
<p>長期典藏屬性，指的是<strong>適合持有、傳承，具備穩定的長期流通基礎</strong>。它是資產與消費的分界線。</p>

<h2>2. 三個檢驗點，各檢驗什麼？</h2>
<table>
<colgroup><col style="width:28%"><col style="width:72%"></colgroup>
<thead><tr><th>檢驗</th><th>說明</th></tr></thead>
<tbody>
<tr><td>適合持有</td><td>保存、養護成本可控，能長期放著。</td></tr>
<tr><td>適合傳承</td><td>能一代一代傳下去，不易耗損。</td></tr>
<tr><td>流通基礎</td><td>需要變現時，市場有人接、有價格。</td></tr>
</tbody>
</table>

<h2>3. 消費與資產的分界，在哪？</h2>
<div class="callout"><div class="ico">肆</div><div><strong>買來用完就沒了的，叫消費；買來放得住、傳得下去的，才叫資產。</strong></div></div>

<h2>4. 一句話記住：怎麼判斷能傳承？</h2>
<p>問自己：<strong>這東西，十年後還在嗎？能傳給下一代嗎？</strong>都行，才過得了這一關。</p>
""",
}

# ============================================================
# 五大全流程服務
# ============================================================
def service_side(current):
    items = [("全流程服務總覽","index.html","index"),
             ("多元資產配置諮詢","allocation.html","allocation"),
             ("標的價值盡調","due-diligence.html","due-diligence"),
             ("藏家私密媒合","matchmaking.html","matchmaking"),
             ("持有規劃","holding-plan.html","holding-plan"),
             ("市場觀察","market-watch.html","market-watch")]
    lis = ""
    for t,u,k in items:
        cls = "active" if k == current else ""
        lis += f'<li><a class="{cls}" href="{u}">{t}</a></li>'
    return '<div class="box"><img class="box-img" src="assets/img/service.webp" alt="五大服務" loading="lazy"><h4>五大服務</h4><ul>' + lis + "</ul></div>"

PAGES["service-index"] = {
    "out_dir": "service", "file": "index.html",
    "title": "五大全流程典藏服務｜9Turn 九回錦",
    "desc": "9Turn 九回錦五大全流程典藏服務：多元資產配置諮詢、標的價值盡調、藏家私密媒合、持有規劃、市場觀察。",
    "kw": "9Turn,九回錦,全流程服務,資產配置,價值盡調,私密媒合,持有規劃",
    "section": "五大服務",
    "crumb": [("首頁","../index.html"), ("五大服務","../service/index.html")],
    "h1": "五大全流程典藏服務：為什麼從買到傳要一路陪到底？",
    "lede": "典藏不是「買到就結束」。從資產配置、盡調、媒合、持有規劃到市場觀察，9Turn 提供完整的全流程服務。",
    "prev": ("長期典藏屬性","../criteria/longterm.html"),
    "next": ("多元資產配置諮詢","allocation.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/service.webp" alt="9Turn 九回錦五大全流程典藏服務" loading="lazy" width="800" height="600"><figcaption>五大服務總覽｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 典藏是一趟旅程，不是一個瞬間？</h2>
<p>很多人以為典藏就是「挑對東西、刷卡買下」。其實真正的典藏，是<strong>從配置、盡調、媒合、持有到傳承的完整旅程</strong>。九回錦把這趟旅程拆成五大服務。</p>

<h2>2. 五大服務一覽：各管哪一段？</h2>
<table>
<colgroup><col style="width:22%"><col style="width:38%"><col style="width:40%"></colgroup>
<thead><tr><th>服務</th><th>一句話</th><th>解決什麼痛點</th></tr></thead>
<tbody>
<tr><td><strong>多元資產配置諮詢</strong></td><td>九大硬資產組合規劃。</td><td>不知道怎麼分散佈局。</td></tr>
<tr><td><strong>標的價值盡調</strong></td><td>真偽驗證、溯源、基本面研究。</td><td>怕買錯、怕買到假的。</td></tr>
<tr><td><strong>藏家私密媒合</strong></td><td>買方與賣方一對一媒合。</td><td>好東西找不到對的人。</td></tr>
<tr><td><strong>持有規劃</strong></td><td>保存、保養、倉儲、傳承架構。</td><td>買到了不知道怎麼守。</td></tr>
<tr><td><strong>市場觀察</strong></td><td>九大硬資產長期市場報告。</td><td>不知道何時該出手、該等。</td></tr>
</tbody>
</table>

<h2>3. 一句話記住：我們的承諾是什麼？</h2>
<div class="callout"><div class="ico">◎</div><div><strong>從買到傳，一路陪到底。</strong>這就是九回錦全流程服務的承諾。</div></div>
""",
}

PAGES["service-allocation"] = {
    "out_dir": "service", "file": "allocation.html",
    "title": "多元資產配置諮詢｜九大硬資產組合規劃",
    "desc": "9Turn 九回錦多元資產配置諮詢：九大硬資產組合規劃，建構分散化典藏組合。看懂如何用三維佈局分散風險。",
    "kw": "9Turn,九回錦,資產配置,組合規劃,分散化,九大硬資產",
    "section": "五大服務",
    "crumb": [("首頁","../index.html"), ("五大服務","../service/index.html"), ("多元資產配置諮詢","../service/allocation.html")],
    "h1": "服務一：多元資產配置諮詢——為什麼不能單押一樣？",
    "lede": "九大硬資產組合規劃，幫你建構一套分散化、可傳承的典藏組合。",
    "layout": "2col",
    "sidebar_html": service_side("allocation"),
    "prev": ("全流程服務總覽","index.html"),
    "next": ("標的價值盡調","due-diligence.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/service.webp" alt="9Turn 九回錦多元資產配置諮詢" loading="lazy" width="800" height="600"><figcaption>多元資產配置諮詢｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 為什麼要「配置」，不是「單買」？</h2>
<p>把身家押在單一資產上，風險太集中。好的典藏，是<strong>把九大硬資產做組合規劃</strong>，讓不同屬性的資產互補、分散風險。</p>

<h2>2. 我們怎麼幫你配置？三個原則</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>原則</th><th>做法</th></tr></thead>
<tbody>
<tr><td>三維佈局</td><td>人文、大地、工業三類都納入考量。</td></tr>
<tr><td>分散化</td><td>不同資產互補，降低單一風險。</td></tr>
<tr><td>個性化</td><td>依你的財務、偏好與目標做客製。</td></tr>
</tbody>
</table>

<h2>3. 配置的核心概念是什麼？</h2>
<div class="callout"><div class="ico">配</div><div><strong>人文、大地、工藝，三維佈局典藏資產。</strong>別把雞蛋放一個籃子，也別讓一種資產扛下全部。</div></div>

<h2>4. 一句話帶走：配置的本義是什麼？</h2>
<p>配置不是把最貴的買齊，而是<strong>用對的組合，讓資產組合更穩、更能傳。</strong></p>
""",
}

PAGES["service-due-diligence"] = {
    "out_dir": "service", "file": "due-diligence.html",
    "title": "標的價值盡調｜真偽驗證與基本面研究",
    "desc": "9Turn 九回錦標的價值盡調：真偽驗證、溯源、基本面研究與狀態檢核。買之前，先把每樣東西查清楚。",
    "kw": "9Turn,九回錦,價值盡調,真偽驗證,溯源,基本面研究",
    "section": "五大服務",
    "crumb": [("首頁","../index.html"), ("五大服務","../service/index.html"), ("標的價值盡調","../service/due-diligence.html")],
    "h1": "服務二：標的價值盡調——為什麼買前一定要查清楚？",
    "lede": "真偽驗證、溯源、基本面研究與狀態檢核——買之前，先把每樣東西查清楚。",
    "layout": "2col",
    "sidebar_html": service_side("due-diligence"),
    "prev": ("多元資產配置諮詢","allocation.html"),
    "next": ("藏家私密媒合","matchmaking.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/service.webp" alt="9Turn 九回錦標的價值盡調" loading="lazy" width="800" height="600"><figcaption>標的價值盡調｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 盡調是做什麼？白話一次講懂</h2>
<p>標的價值盡調，白話講就是<strong>「買東西前，先把它徹底查一遍」</strong>。四大工作：真偽驗證、溯源、基本面研究、狀態檢核。</p>

<h2>2. 四大盡調工作，各查什麼？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>工作</th><th>內容</th></tr></thead>
<tbody>
<tr><td>真偽驗證</td><td>確認東西是真的，不是仿品。</td></tr>
<tr><td>溯源</td><td>來源清楚、文件齊全。</td></tr>
<tr><td>基本面研究</td><td>它的底層價值與市場位置。</td></tr>
<tr><td>狀態檢核</td><td>品相、保存狀態是否良好。</td></tr>
</tbody>
</table>

<h2>3. 盡調為什麼重要？</h2>
<div class="callout"><div class="ico">查</div><div><strong>買錯一項，等於把錢丟進水裡。</strong>盡調是保護你每一分錢的關卡。</div></div>

<h2>4. 一句話帶走：盡調的底線是什麼？</h2>
<p>盡調做足，才敢下手。<strong>查不清楚的，寧可不買。</strong></p>
""",
}

PAGES["service-matchmaking"] = {
    "out_dir": "service", "file": "matchmaking.html",
    "title": "藏家私密媒合｜買賣雙方一對一媒合",
    "desc": "9Turn 九回錦藏家私密媒合：買方與賣方一對一媒合，重視隱私與信任，讓好東西找到對的人。",
    "kw": "9Turn,九回錦,私密媒合,藏家,一對一,隱私",
    "section": "五大服務",
    "crumb": [("首頁","../index.html"), ("五大服務","../service/index.html"), ("藏家私密媒合","../service/matchmaking.html")],
    "h1": "服務三：藏家私密媒合——為什麼好東西要低調成交？",
    "lede": "買方與賣方一對一媒合，讓好東西找到對的人，也讓對的人擁有對的東西。",
    "layout": "2col",
    "sidebar_html": service_side("matchmaking"),
    "prev": ("標的價值盡調","due-diligence.html"),
    "next": ("持有規劃","holding-plan.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/service.webp" alt="9Turn 九回錦藏家私密媒合" loading="lazy" width="800" height="600"><figcaption>藏家私密媒合｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 媒合是什麼？白話一次講懂</h2>
<p>藏家私密媒合，是<strong>買方與賣方的一對一媒合</strong>。不走公開叫賣，而是一對一撮合，重視信任與隱私。</p>

<h2>2. 我們怎麼做媒合？三個關鍵</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>關鍵</th><th>做法</th></tr></thead>
<tbody>
<tr><td>精準匹配</td><td>依雙方的需求與資產條件做配對。</td></tr>
<tr><td>私密進行</td><td>交易細節保密，顧及藏家隱私。</td></tr>
<tr><td>信任為本</td><td>盡調先行，雙方都放心。</td></tr>
</tbody>
</table>

<h2>3. 為什麼要走私密媒合？</h2>
<div class="callout"><div class="ico">配</div><div><strong>好的硬資產，值得低調成交。</strong>私密媒合讓好東西被對的人擁有，不被炒作攪局。</div></div>

<h2>4. 一句話帶走：媒合的本質是什麼？</h2>
<p>私密媒合，讓<strong>「對的東西」找到「對的人」</strong>，低調、信任、穩妥。</p>
""",
}

PAGES["service-holding-plan"] = {
    "out_dir": "service", "file": "holding-plan.html",
    "title": "持有規劃｜保存 保養 倉儲 傳承架構",
    "desc": "9Turn 九回錦持有規劃：藏品保存、保養、倉儲與家族資產傳承架構建議。買到了，更要懂怎麼守。",
    "kw": "9Turn,九回錦,持有規劃,保存保養,倉儲,家族資產,傳承",
    "section": "五大服務",
    "crumb": [("首頁","../index.html"), ("五大服務","../service/index.html"), ("持有規劃","../service/holding-plan.html")],
    "h1": "服務四：持有規劃——為什麼買到了更要懂怎麼守？",
    "lede": "藏品保存、保養、倉儲與家族資產傳承架構建議——買到了，更要懂怎麼守。",
    "layout": "2col",
    "sidebar_html": service_side("holding-plan"),
    "prev": ("藏家私密媒合","matchmaking.html"),
    "next": ("市場觀察","market-watch.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/service.webp" alt="9Turn 九回錦持有規劃" loading="lazy" width="800" height="600"><figcaption>持有規劃｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 持有不是放著不管？為什麼？</h2>
<p>很多資產買來沒好好守，反而耗損價值。持有規劃，就是<strong>教你把藏品守好、守住、傳下去</strong>。</p>

<h2>2. 持有規劃涵蓋什麼？四個面向</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>面向</th><th>內容</th></tr></thead>
<tbody>
<tr><td>保存</td><td>正確的存放環境與條件。</td></tr>
<tr><td>保養</td><td>定期的清潔、維護與修復。</td></tr>
<tr><td>倉儲</td><td>安全的存放與保管方案。</td></tr>
<tr><td>傳承架構</td><td>家族資產如何一代代傳下去。</td></tr>
</tbody>
</table>

<h2>3. 為什麼傳承是終極目標？</h2>
<div class="callout"><div class="ico">守</div><div><strong>典藏的最後一站，是傳給下一代。</strong>好的持有規劃，讓資產守得住、傳得下去。</div></div>

<h2>4. 一句話帶走：買和守，哪個難？</h2>
<p>買得好是本事，<strong>守得住才是真功夫。</strong></p>
""",
}

PAGES["service-market-watch"] = {
    "out_dir": "service", "file": "market-watch.html",
    "title": "市場觀察｜九大硬資產長期市場報告",
    "desc": "9Turn 九回錦市場觀察：九大典藏硬資產長期市場報告。用數據與研究，幫你掌握市場輪轉與價值趨勢。",
    "kw": "9Turn,九回錦,市場觀察,市場報告,硬資產趨勢,市場輪轉",
    "section": "五大服務",
    "crumb": [("首頁","../index.html"), ("五大服務","../service/index.html"), ("市場觀察","../service/market-watch.html")],
    "h1": "服務五：市場觀察——為什麼典藏也要看行情？",
    "lede": "九大硬資產長期市場報告——用數據與研究，幫你看懂市場輪轉。",
    "layout": "2col",
    "sidebar_html": service_side("market-watch"),
    "prev": ("持有規劃","holding-plan.html"),
    "next": ("知識體系","../knowledge/index.html"),
    "body": """
<figure class="asset-fig"><img src="assets/img/service.webp" alt="9Turn 九回錦市場觀察" loading="lazy" width="800" height="600"><figcaption>市場觀察｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 為什麼要看市場？</h2>
<p>典藏不等於不看行情。透過<strong>九大硬資產長期市場報告</strong>，我們追蹤市場輪轉，幫藏家掌握時機與趨勢。</p>

<h2>2. 市場觀察看什麼？三個面向</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>面向</th><th>看什麼</th></tr></thead>
<tbody>
<tr><td>長期趨勢</td><td>九大資產的長期價值走向。</td></tr>
<tr><td>市場輪轉</td><td>不同類別的週期變化。</td></tr>
<tr><td>風險提醒</td><td>值得注意的波動與風險。</td></tr>
</tbody>
</table>

<h2>3. 觀察不是預測，為什麼？</h2>
<div class="callout"><div class="ico">看</div><div><strong>我們提供研究與數據，不替你保證獲利。</strong>市場會波動，決策永遠在你。</div></div>

<h2>4. 一句話帶走：看市場為了什麼？</h2>
<p>會看市場，才知道<strong>什麼時候該出手、什麼時候該等待。</strong></p>
""",
}

# ============================================================
# 知識體系（knowledge）
# ============================================================
def knowledge_side(current):
    items = [("知識體系總覽","index.html","index"),
             ("藝術鑑賞入門","art-appreciation.html","art-appreciation"),
             ("地產地段邏輯","estate-logic.html","estate-logic"),
             ("文玩鑑定基礎","antique-authenticity.html","antique-authenticity"),
             ("寶石分級認識","gem-grading.html","gem-grading"),
             ("酒茶熟成學問","wine-aging.html","wine-aging"),
             ("木材溯源課","timber-provenance.html","timber-provenance"),
             ("名錶機芯入門","watch-movement.html","watch-movement"),
             ("樂器聲學原理","instrument-acoustics.html","instrument-acoustics"),
             ("錢幣評級指南","coin-grading.html","coin-grading"),
             ("資產配置知識","asset-allocation.html","asset-allocation"),
             ("風險管理學","risk-management.html","risk-management")]
    lis = ""
    for t,u,k in items:
        cls = "active" if k == current else ""
        lis += f'<li><a class="{cls}" href="{u}">{t}</a></li>'
    return '<div class="box"><img class="box-img" src="assets/img/knowledge.webp" alt="知識體系" loading="lazy"><h4>知識體系</h4><ul>' + lis + "</ul></div>"

def knowledge_page(slug, file, title, h1, lede, desc, kw, prev, next, body):
    PAGES[slug] = {
        "out_dir":"knowledge","file":file,"title":title,"desc":desc,"kw":kw,
        "section":"知識體系",
        "crumb":[("首頁","../index.html"),("知識體系","../knowledge/index.html"),(h1,"../knowledge/"+file)],
        "h1":h1,"lede":lede,"layout":"2col","sidebar_html":knowledge_side(slug.split("-")[-1] if "-" in slug else "index"),
        "prev":prev,"next":next,"body":body,
    }

PAGES["knowledge-index"] = {
    "out_dir":"knowledge","file":"index.html",
    "title":"知識體系｜9Turn 九回錦 硬資產學習總覽",
    "desc":"9Turn 九回錦知識體系總覽：藝術鑑賞、地產邏輯、寶石分級、酒茶熟成、木材溯源、名錶機芯、資產配置與風險管理。",
    "kw":"9Turn,九回錦,知識體系,硬資產,鑑賞,資產配置,風險管理",
    "section":"知識體系",
    "crumb":[("首頁","../index.html"),("知識體系","../knowledge/index.html")],
    "h1":"知識體系：硬資產的門檻，為什麼在「懂」不在錢？",
    "lede":"典藏是有門檻的。知識體系把鑑賞、篩選、持有、風險等學問系統化，帶你從入門一路學到進階。",
    "prev":("常見問答","../appendix/faq.html"),
    "next":("藝術鑑賞入門","art-appreciation.html"),
    "body":"""
<figure class="asset-fig"><img src="assets/img/knowledge.webp" alt="9Turn 九回錦知識體系總覽" loading="lazy" width="800" height="600"><figcaption>知識體系總覽｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 為什麼要有知識體系？</h2>
<p>硬資產的門檻，不在錢，而在<strong>懂</strong>。不懂鑑賞、不懂篩選、不懂持有，再貴的東西也可能買錯。知識體系，就是九回錦送給藏家的一整套學習資源。</p>

<h2>2. 知識體系涵蓋什麼？十一篇一次看</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>知識篇</th><th>解決什麼問題</th></tr></thead>
<tbody>
<tr><td>藝術鑑賞入門</td><td>看懂創作脈絡與原作價值。</td></tr>
<tr><td>地產地段邏輯</td><td>四把尺量一間地產。</td></tr>
<tr><td>文玩鑑定基礎</td><td>分辨真品與仿品。</td></tr>
<tr><td>寶石分級認識</td><td>看懂等級與證書。</td></tr>
<tr><td>酒茶熟成學問</td><td>理解風土與熟成。</td></tr>
<tr><td>木材溯源課</td><td>看懂珍稀木材的門道。</td></tr>
<tr><td>名錶機芯入門</td><td>認識機械工藝的極致。</td></tr>
<tr><td>樂器聲學原理</td><td>理解名家樂器的聲學。</td></tr>
<tr><td>錢幣評級指南</td><td>看懂版別與評級。</td></tr>
<tr><td>資產配置知識</td><td>佈局你的典藏組合。</td></tr>
<tr><td>風險管理學</td><td>看懂波動、守住資產。</td></tr>
</tbody>
</table>

<h2>3. 怎麼學最有效？</h2>
<p>建議先讀<strong>藝術鑑賞入門</strong>與<strong>資產配置知識</strong>建立基礎，再依你感興趣的資產類別深入。每篇都從痛點講起，用大白話把硬學問講清楚。</p>
""",
}

knowledge_page("knowledge-art","art-appreciation.html","藝術鑑賞入門｜從零開始看懂藝術原作",
"藝術鑑賞入門：從零開始，怎麼看懂原作？",
"藝術的價值在創作脈絡。這篇帶你入門：怎麼看原作、怎麼判斷藝術家定位、怎麼看懂來源。",
"9Turn 九回錦藝術鑑賞入門：如何看懂藝術原作、判斷創作脈絡與藝術家定位、認識完整來源的重要性。","藝術鑑賞,藝術原作,創作脈絡,藝術家,9Turn",
("知識體系總覽","index.html"),("地產地段邏輯","estate-logic.html"),
"""
<figure class="asset-fig"><img src="assets/img/art.webp" alt="9Turn 九回錦藝術鑑賞入門" loading="lazy" width="800" height="600"><figcaption>藝術鑑賞入門｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 先打破一個迷思：藝術不是看得順眼就值錢？</h2>
<p>藝術不是「看得順眼就值錢」。<strong>原作的價值，來自不可複製的創作脈絡</strong>——它在藝術史的位置、藝術家的定位、背後的來源故事。</p>

<h2>2. 四個鑑賞步驟，各看什麼？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>步驟</th><th>看什麼</th></tr></thead>
<tbody>
<tr><td>看脈絡</td><td>這件作品在藝術史裡的位置。</td></tr>
<tr><td>看藝術家</td><td>藝術家是否重要、是否代表其關鍵階段。</td></tr>
<tr><td>看來源</td><td>從誰手上來、有無展覽與出版紀錄。</td></tr>
<tr><td>看狀態</td><td>品相是否完整，影響長期價值。</td></tr>
</tbody>
</table>

<h2>3. 入門三問，問什麼？</h2>
<div class="callout"><div class="ico">◎</div><div><strong>來源完整嗎？有藝術史位置嗎？是藝術家重要階段的代表嗎？</strong>三題都過，才值得考慮。</div></div>

<h2>4. 給入門者的提醒：先練什麼？</h2>
<p>多看、多問、多查。鑑賞是門可以學的功夫，<strong>別急著買，先練眼睛。</strong></p>
""")

knowledge_page("knowledge-estate","estate-logic.html","地產地段邏輯｜四把尺量一間地產",
"地產地段邏輯：一間房子，怎麼量才知道值不值？",
"一間房子能否成為資產，不在裝潢。用地段、建築、供給、風險四把尺來量。",
"9Turn 九回錦地產地段邏輯：用地段邏輯、建築價值、供給限制、持有風險四把尺衡量地產的典藏價值。","地產,地段邏輯,稀有地產,建築價值,供給限制,9Turn",
("藝術鑑賞入門","art-appreciation.html"),("文玩鑑定基礎","antique-authenticity.html"),
"""
<figure class="asset-fig"><img src="assets/img/estate.webp" alt="9Turn 九回錦地產地段邏輯" loading="lazy" width="800" height="600"><figcaption>地產地段邏輯｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 別被裝潢騙了？為什麼？</h2>
<p>一間房子的價值，不在貼了多少大理石。<strong>稀缺地段、建築文化價值、區域供給限制與長期基本面</strong>，才是決定它能否成為資產的關鍵。</p>

<h2>2. 四把尺，各量什麼？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>尺</th><th>衡量什麼</th></tr></thead>
<tbody>
<tr><td>地段邏輯</td><td>所在區域是否稀缺、基本面是否穩健。</td></tr>
<tr><td>建築價值</td><td>有無設計或歷史價值。</td></tr>
<tr><td>供給限制</td><td>區域供給是否受限、難以複製。</td></tr>
<tr><td>持有風險</td><td>流通性與長期持有風險。</td></tr>
</tbody>
</table>

<h2>3. 關鍵一句：地段為什麼複製不來？</h2>
<div class="callout"><div class="ico">地</div><div><strong>土地是稀缺的，地段是複製不來的。</strong>好地段只會越來越少。</div></div>

<h2>4. 入門提醒：看地產先問什麼？</h2>
<p>看地產先問：<strong>十年後還值不值？二十年后還能不能傳下去？</strong>裝潢會舊，地段不會。</p>
""")

knowledge_page("knowledge-antique","antique-authenticity.html","文玩鑑定基礎｜分辨真品與仿品",
"文玩鑑定基礎：真品與仿品，怎麼分才不踩雷？",
"古董文玩是傳世百年的時代痕跡。這篇教你基本鑑定概念，看懂真偽的關鍵。",
"9Turn 九回錦文玩鑑定基礎：如何分辨真品與仿品，看懂傳世紀錄、修復歷史與保存狀態。","古董文玩,鑑定,真偽,仿品,傳世,9Turn",
("地產地段邏輯","estate-logic.html"),("寶石分級認識","gem-grading.html"),
"""
<figure class="asset-fig"><img src="assets/img/antique.webp" alt="9Turn 九回錦文玩鑑定基礎" loading="lazy" width="800" height="600"><figcaption>文玩鑑定基礎｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 文玩收藏的，為什麼是「時間」？</h2>
<p>文玩的靈魂，是<strong>流傳百年的時代痕跡</strong>。一件傳世有序的器物，身上帶著歷代的故事，這是仿品模仿不來的。</p>

<h2>2. 四個鑑定關鍵，各看什麼？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>關鍵</th><th>看什麼</th></tr></thead>
<tbody>
<tr><td>真偽鑑定</td><td>排除仿品與後期量產仿古商品。</td></tr>
<tr><td>傳世紀錄</td><td>出土或傳世來源是否清楚。</td></tr>
<tr><td>修復歷史</td><td>歷經哪些修復，影響品相。</td></tr>
<tr><td>保存狀態</td><td>現有保存情況。</td></tr>
</tbody>
</table>

<h2>3. 仿品為什麼不行？</h2>
<div class="callout"><div class="ico">鑑</div><div><strong>仿品再漂亮，也只是「仿」。</strong>沒有時代痕跡、沒有傳世脈絡，就沒有穿越週期的底層價值。</div></div>

<h2>4. 入門提醒：收文玩先問什麼？</h2>
<p>收文玩，<strong>先問來源與傳世，再談美不美。</strong>真偽過不了關，一切免談。</p>
""")

knowledge_page("knowledge-gem","gem-grading.html","寶石分級認識｜看懂等級與證書",
"寶石分級認識：等級與證書，怎麼看才不會被騙？",
"天然寶石的價值在等級。這篇帶你認識克拉、顏色、淨度、切工，與國際證書。",
"9Turn 九回錦寶石分級認識：克拉、顏色、淨度、切工與國際鑑定證書，看懂天然寶石的等級與價值。","寶石分級,天然寶石,鑑定證書,克拉,淨度,9Turn",
("文玩鑑定基礎","antique-authenticity.html"),("酒茶熟成學問","wine-aging.html"),
"""
<figure class="asset-fig"><img src="assets/img/jewelry.webp" alt="9Turn 九回錦寶石分級認識" loading="lazy" width="800" height="600"><figcaption>寶石分級認識｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 寶石的價值，為什麼在等級？</h2>
<p>同樣是寶石，等級差一級，價值差很多。<strong>克拉、顏色、淨度、切工</strong>，是衡量寶石等級的四大面向。</p>

<h2>2. 四大面向，各看什麼？</h2>
<table>
<colgroup><col style="width:20%"><col style="width:80%"></colgroup>
<thead><tr><th>面向</th><th>說明</th></tr></thead>
<tbody>
<tr><td>克拉</td><td>重量，越大越稀有。</td></tr>
<tr><td>顏色</td><td>色澤的純度與鮮豔度。</td></tr>
<tr><td>淨度</td><td>內含物的多少。</td></tr>
<tr><td>切工</td><td>切磨比例，影響火彩與美觀。</td></tr>
</tbody>
</table>

<h2>3. 證書為什麼就是身分證？</h2>
<div class="callout"><div class="ico">寶</div><div><strong>國際鑑定證書，確認天然來源與產地。</strong>沒有證書，再美也難當資產。</div></div>

<h2>4. 入門提醒：買寶石先問什麼？</h2>
<p>買寶石先要證書，再看等級與設計。天然寶石挖一顆少一顆，稀缺是它穿越週期的底氣。</p>
""")

knowledge_page("knowledge-wine","wine-aging.html","酒茶熟成學問｜風土與時間的資產",
"酒茶熟成學問：風土與時間，怎麼讓酒茶越放越值？",
"能成為資產的酒茶靠陳年潛力。這篇帶你認識風土、熟成與倉儲紀錄。",
"9Turn 九回錦酒茶熟成學問：陳年潛力、風土、熟成與倉儲紀錄，看懂老酒老茶為何越放越值。","經典酒茶,陳年老酒,熟成,風土,倉儲,9Turn",
("寶石分級認識","gem-grading.html"),("木材溯源課","timber-provenance.html"),
"""
<figure class="asset-fig"><img src="assets/img/wine-tea.webp" alt="9Turn 九回錦酒茶熟成學問" loading="lazy" width="800" height="600"><figcaption>酒茶熟成學問｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 酒茶的資產邏輯，是什麼？</h2>
<p>能成為資產的酒茶，<strong>不只是好喝，須具備陳年潛力、名廠與完整倉儲紀錄</strong>。它是少數「越放越值」的資產。</p>

<h2>2. 三個關鍵詞，各是什麼？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>關鍵詞</th><th>說明</th></tr></thead>
<tbody>
<tr><td>風土</td><td>產地環境決定的品質基底。</td></tr>
<tr><td>熟成</td><td>時間讓風味與稀缺沉澱。</td></tr>
<tr><td>倉儲紀錄</td><td>存放條件完整，品相才保得住。</td></tr>
</tbody>
</table>

<h2>3. 關鍵一句：時間為什麼是釀造者？</h2>
<div class="callout"><div class="ico">藏</div><div><strong>時間是酒茶的釀造者。</strong>每多放一年，稀缺與品質就多一分。</div></div>

<h2>4. 入門提醒：買老酒老茶先問什麼？</h2>
<p>買老酒老茶先問倉儲紀錄。<strong>存不好，再好的酒茶也變消費品。</strong></p>
""")

knowledge_page("knowledge-timber","timber-provenance.html","木材溯源課｜看懂珍稀木材的門道",
"木材溯源課：珍稀木材的門道，怎麼看才懂？",
"海南黃花梨、小葉紫檀等珍貴大料，靠來源合法與保存狀態支撐價值。這篇教你入門。",
"9Turn 九回錦木材溯源課：海南黃花梨、小葉紫檀等珍稀木材的種類、來源合法性與保存狀態。","頂級原木,海南黃花梨,小葉紫檀,珍稀木材,溯源,9Turn",
("酒茶熟成學問","wine-aging.html"),("名錶機芯入門","watch-movement.html"),
"""
<figure class="asset-fig"><img src="assets/img/timber.webp" alt="9Turn 九回錦木材溯源課" loading="lazy" width="800" height="600"><figcaption>木材溯源課｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 不是所有木頭都值錢？為什麼？</h2>
<p>只有<strong>生長週期長、原生資源枯竭的珍貴大料</strong>才夠格。像海南黃花梨、小葉紫檀，動輒長數十年上百年。</p>

<h2>2. 四個判斷重點，各看什麼？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>來源合法性</td><td>來源合法、可追溯，杜絕盜伐。</td></tr>
<tr><td>木材種類</td><td>是否為珍稀樹種。</td></tr>
<tr><td>紋理</td><td>紋理美感與稀有度。</td></tr>
<tr><td>保存狀態</td><td>有無開裂、蟲蛀。</td></tr>
</tbody>
</table>

<h2>3. 關鍵一句：樹要長多久？</h2>
<div class="callout"><div class="ico">木</div><div><strong>樹要長一百年，砍掉只要一天。</strong>原生資源枯竭、無法速生複製。</div></div>

<h2>4. 入門提醒：收珍稀木材底線是什麼？</h2>
<p>收珍稀木材，<strong>來源合法是底線。</strong>來源不清的再漂亮也不要碰。</p>
""")

knowledge_page("knowledge-watch","watch-movement.html","名錶機芯入門｜認識機械工藝的極致",
"名錶機芯入門：機械工藝的極致，入門怎麼看？",
"經典名錶的價值在機械工藝與限量。這篇帶你入門機芯與選錶邏輯。",
"9Turn 九回錦名錶機芯入門：認識機械腕錶的工藝價值、限量經典與完整保卡的重要性。","經典名錶,機械錶,機芯,限量腕錶,保卡,9Turn",
("木材溯源課","timber-provenance.html"),("樂器聲學原理","instrument-acoustics.html"),
"""
<figure class="asset-fig"><img src="assets/img/watch.webp" alt="9Turn 九回錦名錶機芯入門" loading="lazy" width="800" height="600"><figcaption>名錶機芯入門｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 腕錶的殘酷真相：為什麼多數買來就貶值？</h2>
<p><strong>多數腕錶購入即貶值。</strong>只有少數經典限量款，能隨時間累積價值。選錶當資產，要的是「經典」，不是「熱門」。</p>

<h2>2. 選錶四大重點，各看什麼？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>原始狀態</td><td>保持出廠原貌。</td></tr>
<tr><td>全套保卡</td><td>配件保卡齊全。</td></tr>
<tr><td>維修紀錄</td><td>出廠與維修歷程清楚。</td></tr>
<tr><td>避開炒作熱款</td><td>短期熱度風險大。</td></tr>
</tbody>
</table>

<h2>3. 為什麼經典能增值？</h2>
<div class="callout"><div class="ico">錶</div><div><strong>經典不會退流行，限量不會再增產。</strong>機械工藝的極致＋稀缺發行量。</div></div>

<h2>4. 入門提醒：買名錶先問什麼？</h2>
<p>買名錶當資產，先問<strong>是不是經典限量、保卡紀錄是否完整</strong>。</p>
""")

knowledge_page("knowledge-instrument","instrument-acoustics.html","樂器聲學原理｜理解名家樂器的聲學",
"樂器聲學原理：名家樂器的聲學，怎麼聽懂？",
"名家手工提琴、古典吉他的價值在聲學品質與製琴師。這篇帶你入門。",
"9Turn 九回錦樂器聲學原理：名家手工提琴與古典吉他的製琴師背景、聲學品質與完整來源。","經典樂器,手工提琴,古典吉他,製琴師,聲學,9Turn",
("名錶機芯入門","watch-movement.html"),("錢幣評級指南","coin-grading.html"),
"""
<figure class="asset-fig"><img src="assets/img/instrument.webp" alt="9Turn 九回錦樂器聲學原理" loading="lazy" width="800" height="600"><figcaption>樂器聲學原理｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 樂器也能典藏？為什麼？</h2>
<p><strong>手工頂級提琴、古典吉他等名家製作樂器</strong>，是兼具聲學品質與工藝傳承的硬資產。量產工廠樂器，不列入典藏。</p>

<h2>2. 四個判斷重點，各看什麼？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>重點</th><th>說明</th></tr></thead>
<tbody>
<tr><td>製琴師背景</td><td>名家手作，工藝加持。</td></tr>
<tr><td>聲學品質</td><td>聲音表現是否頂尖。</td></tr>
<tr><td>完整來源</td><td>來源清楚可追溯。</td></tr>
<tr><td>保存狀態</td><td>琴況是否良好。</td></tr>
</tbody>
</table>

<h2>3. 關鍵一句：琴聲為什麼會老？</h2>
<div class="callout"><div class="ico">音</div><div><strong>琴聲會老，反而更醇。</strong>名家手作的聲學傑作，量產模仿不來。</div></div>

<h2>4. 入門提醒：收樂器先問什麼？</h2>
<p>收樂器先問<strong>製琴師、聲學品質、來源</strong>。量產貨再貴，也成不了典藏。</p>
""")

knowledge_page("knowledge-coin","coin-grading.html","錢幣評級指南｜看懂版別與評級",
"錢幣評級指南：版別與評級，怎麼看才知道值不值？",
"珍稀錢幣與典藏珍郵講究版別、品相與權威評級。這篇帶你入門。",
"9Turn 九回錦錢幣評級指南：古錢、珍稀金銀幣、初版郵票的版別、品相與權威評級。","珍稀錢幣,錢幣評級,版別,金銀幣,珍郵,9Turn",
("樂器聲學原理","instrument-acoustics.html"),("資產配置知識","asset-allocation.html"),
"""
<figure class="asset-fig"><img src="assets/img/coin.webp" alt="9Turn 九回錦錢幣評級指南" loading="lazy" width="800" height="600"><figcaption>錢幣評級指南｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 小物件裡，為什麼有大學問？</h2>
<p>一枚古錢、一張初版郵票，看起來小，其實是<strong>版別與品相的雙重講究</strong>。</p>

<h2>2. 三個關鍵，各是什麼？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>關鍵</th><th>說明</th></tr></thead>
<tbody>
<tr><td>版別</td><td>是否為稀有版別、初版罕見。</td></tr>
<tr><td>品相</td><td>保存狀態與完整度。</td></tr>
<tr><td>權威評級</td><td>有無權威機構評級背書。</td></tr>
</tbody>
</table>

<h2>3. 為什麼普通品不算資產？</h2>
<div class="callout"><div class="ico">評</div><div><strong>普通流通幣與一般紀念郵票不納入。</strong>要的是珍稀版別、初版罕見——量多就不值錢。</div></div>

<h2>4. 入門提醒：收錢幣珍郵先問什麼？</h2>
<p>收錢幣珍郵先問<strong>版別、品相、評級</strong>三件事。</p>
""")

knowledge_page("knowledge-allocation","asset-allocation.html","資產配置知識｜佈局你的典藏組合",
"資產配置知識：典藏組合，怎麼佈局才分散風險？",
"用三維佈局與分散化原則，把九大硬資產組出可傳承的組合。",
"9Turn 九回錦資產配置知識：用人文、大地、工業三維佈局與分散化原則，規劃九大硬資產組合。","資產配置,組合規劃,分散化,九大硬資產,9Turn",
("錢幣評級指南","coin-grading.html"),("風險管理學","risk-management.html"),
"""
<figure class="asset-fig"><img src="assets/img/asset.webp" alt="9Turn 九回錦資產配置知識" loading="lazy" width="800" height="600"><figcaption>資產配置知識｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 為什麼要配置？</h2>
<p>把身家押在單一資產上，風險太集中。<strong>把九大硬資產做組合規劃</strong>，讓不同屬性互補、分散風險。</p>

<h2>2. 三維佈局原則，是什麼？</h2>
<div class="callout"><div class="ico">配</div><div><strong>人文、大地、工藝，三維佈局典藏資產。</strong>別把雞蛋放一個籃子。</div></div>

<h2>3. 配置三步驟，怎麼走？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>步驟</th><th>做法</th></tr></thead>
<tbody>
<tr><td>先分三類</td><td>人文、大地、工業各放一些。</td></tr>
<tr><td>再分散</td><td>同類裡也不要押單一資產。</td></tr>
<tr><td>後傳承</td><td>組合要能放得住、傳得下去。</td></tr>
</tbody>
</table>

<h2>4. 一句話記住：配置的本義是什麼？</h2>
<p>配置不是把最貴的買齊，而是<strong>用對的組合，讓資產更穩、更能傳。</strong></p>
""")

knowledge_page("knowledge-risk","risk-management.html","風險管理學｜看懂波動 守住資產",
"風險管理學：波動來了，怎麼守住你的資產？",
"任何資產都有波動。這篇教你管理典藏風險、看懂市場週期。",
"9Turn 九回錦風險管理學：如何管理典藏風險、看懂市場週期，在波動中守住資產。","風險管理,市場週期,市場輪轉,硬資產,9Turn",
("資產配置知識","asset-allocation.html"),("常見問答","../appendix/faq.html"),
"""
<figure class="asset-fig"><img src="assets/img/knowledge.webp" alt="9Turn 九回錦風險管理學" loading="lazy" width="800" height="600"><figcaption>風險管理學｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 風險是真實存在的，為什麼？</h2>
<p>任何資產都會波動。<strong>關鍵不是躲開波動，而是看懂波動、管理風險。</strong></p>

<h2>2. 三大風險面向，各是什麼？</h2>
<table>
<colgroup><col style="width:24%"><col style="width:76%"></colgroup>
<thead><tr><th>面向</th><th>說明</th></tr></thead>
<tbody>
<tr><td>市場週期</td><td>不同類別的週期變化。</td></tr>
<tr><td>流動性</td><td>需要變現時是否有人接。</td></tr>
<tr><td>保存風險</td><td>保存不當導致的耗損。</td></tr>
</tbody>
</table>

<h2>3. 守資產三原則，是什麼？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>原則</th><th>做法</th></tr></thead>
<tbody>
<tr><td>分散</td><td>別押單一資產。</td></tr>
<tr><td>溯源</td><td>只碰來源清楚的。</td></tr>
<tr><td>養護</td><td>保存得當才保得住。</td></tr>
</tbody>
</table>

<h2>4. 一句話記住：怎麼守住資產？</h2>
<div class="callout"><div class="ico">守</div><div><strong>看懂波動，才能守住資產。</strong>決策永遠在你。</div></div>
""")

# ============================================================
# 附錄（appendix）
# ============================================================
def appendix_side(current):
    items = [("附錄總覽","index.html","index"),
             ("術語表 Glossary","glossary.html","glossary"),
             ("台灣法規對照","regulation.html","regulation"),
             ("免責聲明","disclaimer.html","disclaimer"),
             ("溯源指南","provenance-guide.html","provenance-guide"),
             ("保存養護指南","holding-guide.html","holding-guide"),
             ("常見問答 FAQ","faq.html","faq")]
    lis = ""
    for t,u,k in items:
        cls = "active" if k == current else ""
        lis += f'<li><a class="{cls}" href="{u}">{t}</a></li>'
    return '<div class="box"><h4>知識體系</h4><ul>' + lis + "</ul></div>"

def appendix_page(slug, file, title, h1, lede, desc, kw, prev, next, body):
    PAGES[slug] = {
        "out_dir":"appendix","file":file,"title":title,"desc":desc,"kw":kw,
        "section":"知識體系",
        "crumb":[("首頁","../index.html"),("知識體系","../knowledge/index.html"),(h1,"../appendix/"+file)],
        "h1":h1,"lede":lede,"layout":"2col","sidebar_html":appendix_side(file.split(".")[0]),
        "prev":prev,"next":next,"body":body,
    }

PAGES["appendix-index"] = {
    "out_dir":"appendix","file":"index.html",
    "title":"附錄總覽｜9Turn 九回錦 補充資料",
    "desc":"9Turn 九回錦附錄總覽：術語表、台灣法規對照、免責聲明、溯源指南、保存養護指南與常見問答。",
    "kw":"9Turn,九回錦,附錄,術語表,法規,免責聲明,常見問答",
    "section":"知識體系",
    "crumb":[("首頁","../index.html"),("知識體系","../knowledge/index.html")],
    "h1":"附錄：查得到的知識，為什麼要一次放好？",
    "lede":"術語、法規、免責、指南與問答——九回錦把補充資料整理成冊，方便你隨時查。",
    "prev":("風險管理學","../knowledge/risk-management.html"),
    "next":("術語表","glossary.html"),
    "body":"""
<figure class="asset-fig"><img src="assets/img/appendix.webp" alt="9Turn 九回錦附錄總覽" loading="lazy" width="800" height="600"><figcaption>附錄總覽｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 附錄是什麼？</h2>
<p>附錄是九回錦的<strong>補充資料庫</strong>：從術語解釋、法規對照，到免責聲明、保存指南與常見問答，一次放好。</p>

<h2>2. 附錄內容有哪些？六篇一次看</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>附錄篇章</th><th>解決什麼問題</th></tr></thead>
<tbody>
<tr><td>術語表 Glossary</td><td>硬資產相關術語一次查。</td></tr>
<tr><td>台灣法規對照</td><td>資產傳承與稅務的公開法規面向。</td></tr>
<tr><td>免責聲明</td><td>內容屬性與風險提示。</td></tr>
<tr><td>溯源指南</td><td>怎麼查、怎麼看溯源。</td></tr>
<tr><td>保存養護指南</td><td>各類藏品的保存要點。</td></tr>
<tr><td>常見問答 FAQ</td><td>新手最常問的問題。</td></tr>
</tbody>
</table>

<h2>3. 附錄怎麼用？</h2>
<p>查術語、看法規、找指南，都在這裡。遇到不懂的詞，先翻<strong>術語表</strong>；做交易前，記得讀<strong>免責聲明</strong>。</p>
""",
}

appendix_page("appendix-glossary","glossary.html","術語表｜硬資產 相關名詞一次查",
"術語表：硬資產的名詞，為什麼要先搞懂？",
"把九回錦常用的硬資產術語整理成表，遇到不懂的詞，這裡都有答案。",
"9Turn 九回錦術語表：硬資產、三大典藏、九大資產、四大準則、溯源等名詞解釋。","術語表,硬資產,溯源,稀缺性,底層價值,9Turn",
("附錄總覽","index.html"),("台灣法規對照","regulation.html"),
"""
<figure class="asset-fig"><img src="assets/img/appendix.webp" alt="9Turn 九回錦術語表" loading="lazy" width="800" height="600"><figcaption>術語表｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 硬資產是什麼？白話一次講懂</h2>
<p>看得見、摸得著、放得久的實體珍品，承載美學、歷史、工藝與材料本質，可穿越市場週期、世代傳承。</p>

<h2>2. 常用術語表：各是什麼意思？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>術語</th><th>說明</th></tr></thead>
<tbody>
<tr><td>三大典藏</td><td>人文、大地、工業三大價值分類。</td></tr>
<tr><td>九大資產</td><td>九樣具備底層稀缺的硬資產。</td></tr>
<tr><td>四大準則</td><td>稀缺性、底層價值、完整溯源、長期典藏。</td></tr>
<tr><td>稀缺性</td><td>供給有限、無法量產複製。</td></tr>
<tr><td>底層價值</td><td>美學、歷史、工藝、材料或土地本質價值。</td></tr>
<tr><td>完整溯源</td><td>來源清晰、文件脈絡齊全、可追溯。</td></tr>
<tr><td>長期典藏</td><td>適合持有、傳承，具備穩定流通基礎。</td></tr>
<tr><td>硬資產</td><td>穿越市場週期的實體珍品。</td></tr>
<tr><td>盡調</td><td>買前徹底查清楚標的。</td></tr>
<tr><td>私密媒合</td><td>買賣雙方一對一、低調成交。</td></tr>
</tbody>
</table>

<h2>3. 用一句話串起來：九回錦在做什麼？</h2>
<p>九回錦只收<strong>稀缺、有底、溯源、能傳</strong>的硬資產，用三大分類×九大資產做配置，用五大服務陪藏家走完整趟旅程。</p>
""")

appendix_page("appendix-regulation","regulation.html","台灣法規對照｜資產傳承與稅務 公開法規面向",
"台灣法規對照：資產傳承與稅務，哪些法規要先知道？",
"整理與資產傳承、稅務相關的公開法規面向，供藏家作一般性參考（非法律意見）。",
"9Turn 九回錦台灣法規對照：資產傳承與稅務的公開法規面向，供作一般性參考。","法規,台灣,資產傳承,稅務,遺產,9Turn",
("術語表","glossary.html"),("免責聲明","disclaimer.html"),
"""
<figure class="asset-fig"><img src="assets/img/appendix.webp" alt="9Turn 九回錦台灣法規對照" loading="lazy" width="800" height="600"><figcaption>台灣法規對照｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 本頁定位：這頁能當法律意見嗎？</h2>
<p>本頁僅就<strong>公開的一般性法規面向</strong>作整理，供藏家參考，<strong>不構成法律或稅務意見</strong>。具體個案請諮詢專業律師或會計師。</p>

<h2>2. 與資產傳承相關的公開面向，有哪些？</h2>
<table>
<colgroup><col style="width:34%"><col style="width:66%"></colgroup>
<thead><tr><th>面向</th><th>一般性說明</th></tr></thead>
<tbody>
<tr><td>遺產與贈與</td><td>資產傳承可能涉及遺產稅與贈與稅的相關規定。</td></tr>
<tr><td>財產持有</td><td>不同型態資產（動產、不動產）的持有與移轉規範不同。</td></tr>
<tr><td>交易稅務</td><td>買賣資產可能涉及相關稅費，需依個案評估。</td></tr>
<tr><td>家族傳承規劃</td><td>可透過信託、遺囑等工具規劃資產傳承。</td></tr>
</tbody>
</table>

<h2>3. 重要提醒：法規會不會變？</h2>
<div class="callout"><div class="ico">法</div><div><strong>法規會變動，個案各有不同。</strong>涉及重大資產交易或傳承，務必諮詢專業人士，勿單憑本頁作決策。</div></div>

<h2>4. 一句話帶走：專業的事交給誰？</h2>
<p>資產傳承牽涉法規，<strong>專業的事，交給專業的人。</strong></p>
""")

appendix_page("appendix-disclaimer","disclaimer.html","免責聲明｜內容屬性與風險提示",
"免責聲明：這份內容能當投資建議嗎？",
"本網站內容僅為典藏資產美學與價值研究分享，不構成投資建議或獲利保證。",
"9Turn 九回錦免責聲明：網站內容屬性、風險提示與交易審慎評估。","免責聲明,風險提示,投資建議,硬資產,9Turn",
("台灣法規對照","regulation.html"),("溯源指南","provenance-guide.html"),
"""
<figure class="asset-fig"><img src="assets/img/appendix.webp" alt="9Turn 九回錦免責聲明" loading="lazy" width="800" height="600"><figcaption>免責聲明｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 內容屬性：這份內容是什麼？</h2>
<p>本網站內容僅為<strong>典藏資產美學與價值研究分享</strong>，目的在提供知識與參考，<strong>不構成投資建議或獲利保證</strong>。</p>

<h2>2. 風險提示：過去表現能保未來嗎？</h2>
<div class="callout"><div class="ico">警</div><div><strong>各類硬資產價格會隨市場波動，過去表現不代表未來。</strong>交易請自行審慎評估。</div></div>

<h2>3. 讀者責任：你該做什麼？</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>責任</th><th>做法</th></tr></thead>
<tbody>
<tr><td>當參考</td><td>把網站內容當<strong>知識與研究參考</strong>，不作唯一決策依據。</td></tr>
<tr><td>做盡調</td><td>重大交易前，<strong>自行做足盡調</strong>並諮詢專業人士。</td></tr>
<tr><td>盈虧自負</td><td>投資與典藏皆有風險，<strong>盈虧自負</strong>。</td></tr>
</tbody>
</table>

<h2>4. 一句話記住：內容是什麼？</h2>
<p>內容是研究分享，<strong>不是獲利保證</strong>——決策永遠在你。</p>
""")

appendix_page("appendix-provenance","provenance-guide.html","溯源指南｜怎麼查 怎麼看完整溯源",
"溯源指南：完整溯源，怎麼查、怎麼看才對？",
"完整溯源是價值的通行證。這篇教你怎麼查、怎麼看一份資產的來源脈絡。",
"9Turn 九回錦溯源指南：如何查驗資產來源、文件脈絡與權威憑證，判斷完整溯源。","溯源,來源,文件,鑑定證書,通行證,9Turn",
("免責聲明","disclaimer.html"),("保存養護指南","holding-guide.html"),
"""
<figure class="asset-fig"><img src="assets/img/appendix.webp" alt="9Turn 九回錦溯源指南" loading="lazy" width="800" height="600"><figcaption>溯源指南｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 溯源為什麼重要？</h2>
<p>來源不清的資產，就像<strong>沒有戶口的房子</strong>——價值再高也難傳承、難轉手。完整溯源，是價值的通行證。</p>

<h2>2. 怎麼查溯源？四步驟</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>步驟</th><th>做什麼</th></tr></thead>
<tbody>
<tr><td>來源紀錄</td><td>從誰手上來、歷經哪些手。</td></tr>
<tr><td>權威文件</td><td><strong>鑑定證書</strong>、出版圖錄、評級文件。</td></tr>
<tr><td>傳世脈絡</td><td>有無清楚的流傳歷史。</td></tr>
<tr><td>交叉驗證</td><td>多份文件互相佐證。</td></tr>
</tbody>
</table>

<h2>3. 看溯源的四個提醒，各是什麼？</h2>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>提醒</th><th>說明</th></tr></thead>
<tbody>
<tr><td>來源要可追溯</td><td>每一手都能說清楚。</td></tr>
<tr><td>文件要齊全</td><td>證書、紀錄都在。</td></tr>
<tr><td>脈絡要連續</td><td>中間沒有斷層或漏洞。</td></tr>
<tr><td>要多方佐證</td><td>別只憑單一文件。</td></tr>
</tbody>
</table>

<h2>4. 一句話記住：查不清怎麼辦？</h2>
<p>查不清來龍去脈的，<strong>寧可不買。</strong></p>
""")

appendix_page("appendix-holding","holding-guide.html","保存養護指南｜各類藏品的保存要點",
"保存養護指南：各類藏品，怎麼守才不會耗損？",
"藏品保存不當會耗損價值。這篇整理各類硬資產的保存養護要點。",
"9Turn 九回錦保存養護指南：藝術品、珠寶、酒茶、木材、名錶、樂器等藏品的保存養護要點。","保存養護,藏品保存,保養,倉儲,硬資產,9Turn",
("溯源指南","provenance-guide.html"),("常見問答","faq.html"),
"""
<figure class="asset-fig"><img src="assets/img/appendix.webp" alt="9Turn 九回錦保存養護指南" loading="lazy" width="800" height="600"><figcaption>保存養護指南｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 保存是價值的日常功課？為什麼？</h2>
<p>再好的藏品，保存不當也會耗損。正確的保存與養護，是延續藏品價值的關鍵。</p>

<h2>2. 各類藏品保存要點，各是什麼？</h2>
<table>
<colgroup><col style="width:22%"><col style="width:78%"></colgroup>
<thead><tr><th>藏品</th><th>保存要點</th></tr></thead>
<tbody>
<tr><td>藝術品</td><td>避光、控溫濕度，避免溫差劇變。</td></tr>
<tr><td>珠寶</td><td>分格存放，避免碰撞刮傷。</td></tr>
<tr><td>酒茶</td><td>恆溫、避光、恆濕，環境穩定。</td></tr>
<tr><td>木材</td><td>控濕度，避免乾裂與蟲蛀。</td></tr>
<tr><td>名錶</td><td>定期保養，正確上鏈與存放。</td></tr>
<tr><td>樂器</td><td>控溫濕度，避免變形與開裂。</td></tr>
<tr><td>錢幣珍郵</td><td>專業夾頁存放，避免指觸與氧化。</td></tr>
</tbody>
</table>

<h2>3. 通用原則，有哪些？</h2>
<table>
<colgroup><col style="width:26%"><col style="width:74%"></colgroup>
<thead><tr><th>原則</th><th>做法</th></tr></thead>
<tbody>
<tr><td>環境穩定</td><td>恆溫恆濕，避免劇變。</td></tr>
<tr><td>避光避塵</td><td>減少紫外線與塵埃。</td></tr>
<tr><td>專業器具</td><td>用專用夾頁、盒具保存。</td></tr>
<tr><td>定期檢查</td><td>定期檢視品相，及早處理。</td></tr>
</tbody>
</table>

<h2>4. 一句話記住：買和守，哪個難？</h2>
<div class="callout"><div class="ico">養</div><div><strong>買得好是本事，守得住才是真功夫。</strong></div></div>
""")

appendix_page("appendix-faq","faq.html","常見問答｜新手最常問的 9Turn 九回錦問題",
"常見問答：新手最常問的 9Turn 問題，一次答清？",
"把新手最常問的問題一次答清楚，從硬資產是什麼到怎麼開始典藏。",
"9Turn 九回錦常見問答：硬資產是什麼、三大典藏是什麼、怎麼開始典藏、四大準則等新手問題。","常見問答,FAQ,硬資產,怎麼開始典藏,9Turn",
("保存養護指南","holding-guide.html"),("品牌理念","../brand/index.html"),
"""
<figure class="asset-fig"><img src="assets/img/appendix.webp" alt="9Turn 九回錦常見問答" loading="lazy" width="800" height="600"><figcaption>常見問答｜9Turn 九回錦典藏研究</figcaption></figure>

<h2>1. 常見問答：新手最常問的有哪些？</h2>
<table>
<colgroup><col style="width:22%"><col style="width:44%"><col style="width:34%"></colgroup>
<thead><tr><th>問題類型</th><th>你大概在問</th><th>一句話答案</th></tr></thead>
<tbody>
<tr><td>品牌類</td><td>9Turn 九回錦是什麼？做不做短線炒作？</td><td>專注硬資產的典藏平台，只玩有價值的資產。</td></tr>
<tr><td>資產類</td><td>什麼是硬資產？九大資產有哪些？</td><td>看得見、摸得著、放得久的實體珍品。</td></tr>
<tr><td>準則類</td><td>什麼東西才夠格進典藏名單？</td><td>須通過稀缺性、底層價值、完整溯源、長期典藏四大準則。</td></tr>
<tr><td>風險類</td><td>網站內容能當投資建議嗎？</td><td>不能，內容僅為研究分享，不構成投資建議。</td></tr>
<tr><td>起步類</td><td>新手怎麼開始？</td><td>先讀知識體系建立基礎，再依興趣深入。</td></tr>
</tbody>
</table>
<div class="faq">
<details><summary>9Turn 九回錦是什麼？</summary><p>一個專注硬資產的典藏平台，三大典藏×九大珍品，只玩有價值的資產。</p></details>
<details><summary>什麼是硬資產？</summary><p>看得見、摸得著、放得久的實體珍品，可穿越市場週期、世代傳承。</p></details>
<details><summary>三大典藏是哪三類？</summary><p>人文典藏（人類創作）、大地典藏（自然稀缺）、工業典藏（經典工藝）。</p></details>
<details><summary>九大資產有哪些？</summary><p>藝術品、稀有地產、古董文玩、珠寶、酒茶、原木、名錶、樂器、錢幣珍郵。</p></details>
<details><summary>什麼東西才夠格進典藏名單？</summary><p>須通過四大準則：稀缺性、底層價值、完整溯源、長期典藏屬性。</p></details>
<details><summary>你們做短線炒作嗎？</summary><p>不做。只經營具備底層稀缺性的硬資產，就算行情火熱，不符準則不納入。</p></details>
<details><summary>網站內容能當投資建議嗎？</summary><p>不能。內容僅為研究分享，不構成投資建議或獲利保證。</p></details>
<details><summary>新手怎麼開始？</summary><p>先讀知識體系建立基礎，再依感興趣的資產深入，記得先看免責聲明。</p></details>
</div>

<h2>2. 還有疑問？去哪找答案？</h2>
<p>更多內容，歡迎翻閱<strong>品牌理念</strong>與<strong>知識體系</strong>。這裡的每個字，都在把硬資產講給你聽。</p>
""")
