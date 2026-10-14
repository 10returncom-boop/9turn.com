# ArtArchive 藝術典藏圖庫

> 核心分工：**GitHub 放純文字 metadata + 腳本** ｜ **Google Drive 放圖檔** ｜ **本機硬碟做最終備份**

## 1. 分工原則

| 儲存位置 | 放什麼 | 不放什麼 |
|---|---|---|
| **GitHub** | `art_archive.csv`、`_scripts/*.py`、README、.env.example | ❌ 任何大圖／原始圖檔 |
| **Google Drive（專用典藏帳號）** | 原始母檔、WebP 預覽、縮圖三類圖檔 | ❌ metadata、腳本 |
| **本機硬碟** | 完整原始圖備份（最終保險） | — |

## 2. 資料夾結構

```
ArtArchive 藝術典藏圖庫/
├─ 01_OriginalRaw/         原始高清母檔｜完全私密，不開任何分享
│  ├─ A_油畫/
│  ├─ B_雕塑/
│  └─ C_水墨/
├─ 02_WebPreview/          WebP 預覽圖｜「知道連結的人可檢視」，供九回錦網站用
│  ├─ A_油畫/ B_雕塑/ C_水墨/
├─ 03_Thumbnail/           小縮圖｜同樣「知道連結的人可檢視」
│  ├─ A_油畫/ B_雕塑/ C_水墨/
├─ _scripts/               Python 腳本
├─ _docs/                  文件
├─ art_archive.csv         metadata（主索引）
├─ .env.example            環境變數範本
└─ README.md
```

> 每個分類子資料夾控制在 **2000 張以內**，避免 Drive 網頁版卡頓。

## 3. 檔名規範（與 CSV `art_id` 一一對應）

```
ART00001-油畫-莫內-睡蓮-1916.webp
格式：ART<5位數>-<分類>-<作者>-<標題>-<年代>.<副檔名>
```

- 分類取值：`油畫`、`雕塑`、`水墨`
- 標題可含連字號；年份取 4 位數字

## 4. CSV 欄位定義（art_archive.csv）

| 欄位 | 說明 | 由誰填 |
|---|---|---|
| `art_id` | 唯一編號 ART00001… | scan_build_csv 自動 |
| `category` | 分類（油畫/雕塑/水墨） | scan_build_csv 自動 |
| `artist` / `title` / `year` | 作者 / 標題 / 年代 | scan_build_csv 從檔名解析 |
| `filename` | 原始檔名 | 自動 |
| `original_path` / `webp_path` / `thumb_path` | 本機三類路徑 | 自動 |
| `md5_original` / `md5_webp` / `md5_thumb` | 三類 MD5 雜湊 | 自動 |
| `gdrive_original_url` / `gdrive_webp_url` / `gdrive_thumb_url` | Drive 連結 | upload_share_links 回填 |
| `status` | local / uploaded | 腳本更新 |
| `notes` | 備註 | 手動 |

> CSV 以 **UTF-8 帶 BOM** 儲存，Excel 可直接開啟顯示中文。

## 5. 腳本使用流程

先安裝依賴：`python -m pip install -r requirements.txt`

| 步驟 | 指令 | 說明 |
|---|---|---|
| ① 掃描建 CSV | `python _scripts\scan_build_csv.py --source "D:\圖庫來源"` | 掃描、解析、指派 art_id、算 MD5、寫 CSV |
| ② 生成預覽/縮圖 | `python _scripts\make_webp.py` | 從 01_OriginalRaw 產生 WebP 預覽 + 縮圖 |
| ③ 上傳 + 回填連結 | `python _scripts\upload_share_links.py --root-folder-id <ID>` | 上傳 Drive、設權限、回填連結（需憑證） |
| ④ 重建畫廊資料 | `python _scripts\build_art_data.py` | 從 CSV 重建 art_data.js（畫廊索引用） |
| ⑤ 產生獨立作品頁 | `python _scripts\build_work_pages.py` | 每件作品產生 ARTxxxxx.html 獨立頁（SSG） |
| ⑥ 完整性校驗 | `python _scripts\verify_md5.py` | 重算 MD5 比對，揪出被替換/損毀/遺失 |
| （可選）演練 | 加上 `--dry-run` | 只列計畫不實際動作 |

完成後把 `art_archive.csv` commit、push 到 GitHub。

## 6. 前置設定（建立專用典藏帳號後）

1. **註冊全新 Google 帳號**專做 ArtArchive，與個人帳號完全隔離。
2. **開啟 2FA（兩步驗證）**，優先硬體安全金鑰（YubiKey），其次 Google Authenticator。
3. 安裝 **Google Drive for Desktop**，把 ArtArchive 掛成本機磁碟（供大量上傳/備份）。
4. **GitHub**：建立私有儲存庫，放 CSV + 腳本（不放圖）。
5. **Drive API 授權**（給 upload_share_links.py）：
   - Google Cloud Console 開專案 → 啟用 Google Drive API
   - 建立「服務帳號」，下載 JSON 憑證
   - 在專用 Drive 把 ArtArchive 資料夾「共用」給服務帳號 email（權限：編輯者）
   - 把 JSON 憑證路徑寫入 `.env` 的 `SERVICE_ACCOUNT_FILE`（**勿 commit 進 GitHub**）

## 7. 安全規則

1. 獨立專用帳號放典藏，與個人帳號隔離（最重要）。
2. 帳號開 2FA、獨一無二密碼、只用來跑典藏庫。
3. 權限分級：原始母檔完全私密；預覽/縮圖「知道連結的人可檢視」，**不開放搜尋索引**。
4. 本機硬碟保留完整原始圖備份；雲端是第二備份，不是唯一存放點。
5. metadata 在 GitHub 有版本紀錄，獨立於雲端。
6. 定期執行 `verify_md5.py` 校驗。

## 8. 網站串接（九回錦）對策

- 前端讀 GitHub `art_archive.csv`，只載 WebP 預覽與縮圖，**永不載原始大母檔**。
- GDrive 大量嵌入有流量上限，高流量會回 403；流量成長後把預覽圖遷到 CDN，GDrive 退居後備典藏。

## 9. 已知限制

- Google Drive 非企業 DAM，權限只能以資料夾為單位，無法單張作品設不同權限。
- 大量嵌入 GDrive 圖有流量門檻。
- 若帳號違反服務條款被限制，雲端圖會暫時無法存取；本機備份即對應此風險。
