# -*- coding: utf-8 -*-
"""刪除 content.py 的 50 大功能區塊（行 1219-1633）"""
p = r"D:\_WWW_325_public\9turn.com九回錦3\content.py"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()
# 確認邊界
print("A119:", repr(lines[1218]))
print("A1633:", repr(lines[1632]))
print("A1634:", repr(lines[1633]))
# 刪行 1219..1633（0-based index 1218..1632）
del lines[1218:1633]
with open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("after-A1634:", repr(lines[1218]))
print("done, len", len(lines))
