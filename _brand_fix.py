# -*- coding: utf-8 -*-
"""全站品牌名統一：9TURN → 9Turn（py 源檔 + css/js 註釋）"""
import os, glob

ROOT = r"D:\_WWW_325_public\9turn.com九回錦3"
targets = ["core.py", "content.py", "content_deep.py",
           "assets/css/style.css", "assets/js/main.js"]
targets += glob.glob(os.path.join(ROOT, "deep_data", "*.py"))

cnt = 0
for name in targets:
    p = name if os.path.isabs(name) else os.path.join(ROOT, name)
    if not os.path.exists(p):
        continue
    with open(p, encoding="utf-8") as f:
        s = f.read()
    n = s.count("9TURN")
    if n:
        s = s.replace("9TURN", "9Turn")
        with open(p, "w", encoding="utf-8") as f:
            f.write(s)
        cnt += n
        print(f"{os.path.relpath(p, ROOT)}: {n} 處")
print("total", cnt)
