# 9Turn 九回錦｜內容層改版規格 v1（Subagent 必讀）

> 本規格由 OrganizeAgent 依示範頁凍結。改版只動內容源檔案：`content.py`、`deep_data/*.py`。
> **`core.py`、`verify.py`、`content_deep.py`、`assets/` 一律不准動**（content_deep.py 與 assets 由 OrganizeAgent 另行處理）。
> 改完必須通過下述「交付自檢」才可回報完成。

## 0. 三個示範（先讀，照這個質感做）
- 主站示範：`content.py` 的 `brand-positioning`（PAGES["brand-positioning"]）、`criteria-scarcity`
- 深度示範：`deep_data/art.py` 第 01 篇（三支柱比較表格）
示範已含：問句 H1／編號問句 H2／比較表格／asset-fig 插圖／粗體／大白話。你的改法要與示範同級。

## 1. 語言（硬約束）
- 純正台灣繁體中文、台灣用語（如「資訊、軟體、單元、影片、佔比、績效」；避免簡體字與大陸用語）。
- 大白話、痛點開頭、解惑式；像資深藏家朋友跟你講話，不是教科書。
- 禁止 AI 樣板句：不得以「首先／其次／最後」做三段式結構；不得出現「本文將介紹」「接下來，讓我們」「總而言之」「綜上所述」「眾所周知」「隨著現代」等無資訊過渡。
- 「最後提醒」「最後一句」這類口語過渡可保留，但同一篇文章內不得連用兩次以上；如出現請改寫成「還有一件事要注意」「別忘了」等。

## 2. 標題（H1/H2/H3）
- H1：保留「主題：」前綴，後半改為問句＋數字感。範例：
  - `品牌定位：只玩有價值的資產` → `品牌定位：為什麼我們只玩有價值的資產？`
  - `準則一：稀缺性——供給有限，無法量產複製` → `準則一：稀缺性——為什麼供給有限、無法複製才算資產？`
- H2：保留「1. 2. 3. …」流水編號，標題句改問句風格（含「為什麼／怎麼／哪」）。範例：
  - `2. 三種稀缺來源` → `2. 稀缺從哪來？三種來源一次看`
  - `4. 一句話記住` → `4. 一句話記住：先問它能不能被複製`
- H3：保持「3.1」子編號，同樣問句化。
- 功能性頁面（術語表／免責聲明／常見問答等）H1 也改問句但須合理，例如：
  - `免責聲明：內容屬性與風險提示` → `免責聲明：這份內容能當投資建議嗎？`
- 改標題同時更新同頁 `desc`／`lede` 讓語意一致（若原本已對應可不動）；**不得改 `file`、`slug`、`out_dir`、`crumb` 網址**。

## 3. 比較表格（重點增量）
- 每頁／每篇文章至少 1 個 HTML `<table>` 比較 2–3 項；深度專區缺表格的篇章必須補。
- 表格內容從該頁既有論點提煉比較維度（如「支柱／撐住什麼／缺了它的下場」「類型／說明」「檢查點／用的工具／看什麼」），**不許引入文章沒有的新主題**。
- 表格可用 `<colgroup>` 設寬度；`<thead>` 加 `<th>`；文字定性描述為主。
- **禁止編造精確數字**：表格與內文都不得出現查無來源的具體金額／年份／百分比。需要數字時寫「約…」「據公開報導…」或改用定性比較。已知可查證案例（如張大千《桃源圖》2016 年香港約 2.7 億港元成交、達文西《救世主》等）可沿用，其餘一律保守。

## 4. 可核實案例（增量）
- 主站頁面若談到價值／行情／鑑定，補 1 個公開可查的案例（拍賣紀錄、真實藏品、法規）或知名軼事，並註明「據公開報導／據傳」。
- 找不到來源就寫定性描述，寧缺勿假。

## 5. 專有名詞粗體
- 對專有名詞加 `<strong>`：張大千、GIA 證書、CITES、骨董、陀飛輪、拍賣紀錄、鑑定證書、condition report、catalogue raisonné、范米格倫（Han van Meegeren）、蘇富比、佳士得等（含該資產領域的術語）。
- 已加粗的不重複包一層；避免把整句包成粗體（只包名詞）。

## 6. 插圖（asset-fig）— 主站頁面才做
- `content.py` 主站頁面 body 中若無 `<figure class="asset-fig">`，在開頭段落之後補 1 張，格式：
  `<figure class="asset-fig"><img src="assets/img/XXX.webp" alt="…" loading="lazy" width="800" height="600"><figcaption>…｜9Turn 九回錦典藏研究</figcaption></figure>`
- 圖片對應表（`assets/img/` 內已有）：
  - 品牌 5 頁 → `brand.webp`（OrganizeAgent 將生成）
  - 三大分類 4 頁 → `category.webp`（將生成）
  - 九大資產總覽 → `asset.webp`（將生成）
  - 四大準則 5 頁 → `criteria.webp`（將生成）
  - 五大服務 6 頁 → `service.webp`（將生成）
  - 知識體系 11 篇 → 對應資產圖：art→`art.webp`、estate→`estate.webp`、antique→`antique.webp`、gem→`jewelry.webp`、wine→`wine-tea.webp`、timber→`timber.webp`、watch→`watch.webp`、instrument→`instrument.webp`、coin→`coin.webp`、allocation→`asset.webp`、risk→`knowledge.webp`（將生成）
  - 附錄 7 頁 → `appendix.webp`（將生成）
  - 深度專區文章：已有 `assets/img/<資產>.webp` 插圖，**不用再加**（避免重複）。
- alt 用繁體描述；figcaption 以「｜9Turn 九回錦典藏研究」結尾。

## 7. 交付自檢（每項都要做）
1. `python -c "import content"` 可正常載入（改 content.py 時）。
2. `python -c "import deep_data.<模組>"` 可正常載入（改 deep_data 時）。
3. 全站斷鏈不得新增：你新增的任何 `src`／`href` 檔案必須真實存在於 `assets/img/`（可用 PowerShell `Test-Path` 驗證相對本機路徑）。
4. 回報格式：改動檔案清單＋每檔改了哪些（H1 數／表格數／插圖數／樣板句清理數）＋自檢結果。
