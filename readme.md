# 9TURN 九回錦｜官方網站

**只玩有價值的資產。** 三大典藏、九大珍品，專注可穿越市場週期、世代傳承的硬資產典藏平台。

純 HTML/CSS/JS 靜態網站，無後端依賴，可直接部署至 **GitHub Pages**。全站 **309 頁**，繁體中文（zh-Hant）、UTF-8 編碼。

---

## 快速開始

```powershell
# 1. 重建全站（合併主站＋深度專區，同步 assets，產生 SEO 檔）
python core.py

# 2. 三項批次檢核（SEO 元素／斷鏈／本機檔案獨立性）
python verify.py
```

開啟首頁 `index.html` 即為完整網站。

## 網站架構

| 資料夾 | 主題 | 頁數 |
| --- | --- | --- |
| / | 首頁、網站地圖、404、SEO 檔 | 3＋ |
| brand/ | 品牌理念 | 5 |
| category/ | 三大分類 | 4 |
| asset/ | 九大資產主頁 | 10 |
| asset/<key>/ | 九大資產深度專區（9 × 22 篇） | 207 |
| criteria/ | 四大準則 | 5 |
| service/ | 五大服務 | 6 |
| feature/ | 50 大功能 | 50 |
| knowledge/ | 知識體系 | 12 |
| appendix/ | 附錄 | 7 |

**資料夾規則**：一個大主題 = 一個子資料夾；每資料夾都有 `index.html`，搬移資料夾時依然獨立成站（每資料夾自含 assets、sitemap.xml、manifest）。

## 內容與維護

- **主站內容**：`content.py`（品牌／分類／資產／準則／服務／50 大功能／知識／附錄）
- **深度專區內容**：`deep_data/<key>.py`（每資產 22 篇 ARTICLES）
- **生成器與設計系統**：`core.py`、`assets/css/style.css`、`assets/js/main.js`
- **全站變數與導覽**：`core.py` 的 `SITE`、`NAV`（完整對照見 CONTENT-SPEC.md）
- **規格書**：`CONTENT-SPEC.md`（網站變數、導覽、地圖、內容規範、批次更新機制）

改內容後 `python core.py` 一鍵重建，`python verify.py` 檢核通過即可上線。

## SEO 重點

- 每頁獨立 title／description／canonical／OG（OG=9）／JSON-LD（≥3 種結構化資料）
- Breadcrumb＋BreadcrumbList Schema、FAQPage
- 全站 sitemap.xml／robots.txt／manifest.webmanifest／404.html
- WebP 圖片、lazy loading、語意化 alt

## 授權與聲明

本網站內容僅為典藏資產美學與價值研究分享，不構成投資建議或獲利保證；各類硬資產價格會隨市場波動，交易請自行審慎評估。

© 2026 9TURN 九回錦｜九回見錦，價值歷循環而不減
