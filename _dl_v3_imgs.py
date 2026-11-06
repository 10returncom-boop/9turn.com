# -*- coding: utf-8 -*-
"""下載 v3 滿版底圖(13)＋og-cover，轉壓縮 WebP 存入 assets/img/"""
import os, urllib.request, io
from PIL import Image

OUT = r"D:\_WWW_325_public\9turn.com九回錦3\assets\img"
os.makedirs(OUT, exist_ok=True)

MAP = {
    "bg-01.webp": "https://aka.doubaocdn.com/s/d4mjUSXVK9",
    "bg-02.webp": "https://aka.doubaocdn.com/s/3cRxGGEGhf",
    "bg-03.webp": "https://aka.doubaocdn.com/s/rRh1OGC7M1",
    "bg-04.webp": "https://aka.doubaocdn.com/s/rea29LVKtv",
    "bg-05.webp": "https://aka.doubaocdn.com/s/88XoBEavUv",
    "bg-06.webp": "https://aka.doubaocdn.com/s/D2NrvqGC5a",
    "bg-07.webp": "https://aka.doubaocdn.com/s/WP1ZXyJaBY",
    "bg-08.webp": "https://aka.doubaocdn.com/s/tygByIb4qE",
    "bg-09.webp": "https://aka.doubaocdn.com/s/CAUl8adiwm",
    "bg-10.webp": "https://aka.doubaocdn.com/s/Llfn38IOSE",
    "bg-11.webp": "https://aka.doubaocdn.com/s/hisxbmawvm",
    "bg-12.webp": "https://aka.doubaocdn.com/s/QulLwyUyIt",
    "bg-13.webp": "https://aka.doubaocdn.com/s/RTmnwJAliV",
    "og-cover.webp": "https://aka.doubaocdn.com/s/WLXUNlMFNn",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=60).read()

for name, url in MAP.items():
    try:
        data = fetch(url)
        im = Image.open(io.BytesIO(data)).convert("RGB")
        q = 72 if name.startswith("bg-") else 80
        im.save(os.path.join(OUT, name), "WEBP", quality=q, method=6)
        print(name, im.size, "ok")
    except Exception as e:
        print(name, "ERR", e)
