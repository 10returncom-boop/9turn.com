# -*- coding: utf-8 -*-
"""延伸閱讀卡(rel-card)去圖改漸層：
1) 刪除所有 .rel-card[href=...]{background-image:url(...)} 配圖規則
2) .rel-card 改品牌漸層背景（保留文字 rc-tag/rc-title）
3) 移除 .box-img 規則（側欄圖已移除）
保留 line 460 .asset-fig figcaption。
"""
import io, re

P = r"D:\_WWW_325_public\9turn.com九回錦3\assets\css\style.css"
s = io.open(P, encoding="utf-8").read()

# 1) 刪除所有 rel-card 配圖行
before = s.count("rel-card[href=")
s2 = re.sub(r'^\.rel-card\[href=[^\n]*?\]\{background-image:url\([^\n]*?\)\}\s*$\n?', '', s, flags=re.M)

# 2) 替換 .rel-card 塊與 ::after 遮罩 → 品牌漸層
old_block = """.rel-card{position:relative;overflow:hidden;border:none;padding:0;min-height:148px;
  background-color:var(--ink-deep);background-size:cover;background-position:center;
  box-shadow:0 6px 18px rgba(8,23,18,.18)}"""
new_block = """.rel-card{position:relative;overflow:hidden;border:1px solid rgba(255,255,255,.12);padding:18px 18px;min-height:118px;display:flex;flex-direction:column;
  background:linear-gradient(135deg,#1D3B32,#0E2A23 55%,#162622);box-shadow:0 6px 18px rgba(8,23,18,.18)}"""
assert old_block in s2, "找不到 .rel-card 覆寫塊"
s2 = s2.replace(old_block, new_block)

old_after = """.rel-card::after{content:"";position:absolute;inset:0;z-index:1;
  background:linear-gradient(180deg,rgba(8,23,18,.06) 0%,rgba(8,23,18,.84) 80%)}"""
new_after = """.rel-card::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;
  background:linear-gradient(120deg,rgba(201,162,39,.12),rgba(8,23,18,0) 55%)}"""
if old_after in s2:
    s2 = s2.replace(old_after, new_after)

io.open(P, "w", encoding="utf-8", newline="").write(s2)

chk = io.open(P, encoding="utf-8").read()
print("刪除配圖規則:", before - chk.count("rel-card[href="), "條；剩", chk.count("rel-card[href="), "條")
print(".box-img 剩:", chk.count(".box-img"))
