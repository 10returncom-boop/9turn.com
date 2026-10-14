# -*- coding: utf-8 -*-
import os, shutil
root = r"D:\_WWW_325_public\9turn.com九回錦3"
src = os.path.join(root, "assets", "css", "style.css")
src_bytes = open(src, "rb").read()
cnt = 0
for dirpath, dirnames, filenames in os.walk(root):
    if "_shots" in dirpath or "_backup" in dirpath or ".git" in dirpath:
        continue
    if "assets" in dirnames and "css" in os.listdir(os.path.join(dirpath, "assets")):
        dst = os.path.join(dirpath, "assets", "css", "style.css")
        if os.path.exists(dst) and os.path.abspath(dst) != os.path.abspath(src):
            open(dst, "wb").write(src_bytes)
            cnt += 1
print("同步子資料夾 style.css 數量:", cnt)
