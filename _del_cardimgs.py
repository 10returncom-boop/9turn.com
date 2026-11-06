# -*- coding: utf-8 -*-
"""移除內容層誤加的卡片配圖 CSS 區塊（使用者已否決內頁卡片圖）。
保留 line 460 既有的 .asset-fig figcaption 規則；只移除其尾端註釋與 461-690 的
.rel-card 背景圖 / box-img / 深色 overlay 規則。"""
import io

P = r"D:\_WWW_325_public\9turn.com九回錦3\assets\css\style.css"
s = io.open(P, encoding="utf-8").read()
lines = s.split("\n")

# line 460（1-based）= index 459：移除尾端「}/* ========== 內容層改版追加… */」
i = 459
assert lines[i].endswith("*/"), f"預期 line 460 尾端註釋，實際: {lines[i][-60:]}"
cut = lines[i].rfind("}/*")
assert cut > 0, "找不到 }/* 分隔點"
lines[i] = lines[i][: cut + 1]

# 刪除 461-690（1-based）＝ index 460-689
assert lines[460].lstrip().startswith(".rel-card{position:relative"), "預期 461 行是 .rel-card 覆寫"
keep = lines[: i + 1] + lines[690:]
out = "\n".join(keep)
io.open(P, "w", encoding="utf-8", newline="").write(out)

# 驗證
chk = io.open(P, encoding="utf-8").read()
assert "rel-card[href=" not in chk, "rel-card 背景圖規則未完全移除"
assert ".box-img" not in chk, "box-img 規則未移除"
assert "內容層改版追加" not in chk, "註釋未移除"
print(f"移除完成：{len(lines)} 行 → {len(keep)} 行；rel-card[href]={chk.count('rel-card[')} 條")
