# -*- coding: utf-8 -*-
import os, urllib.request, sys
ROOT = r"D:\_WWW_325_public\9turn.com九回錦3"
IMG = os.path.join(ROOT, "assets", "img")
os.makedirs(IMG, exist_ok=True)
imgs = {
    "art":        "https://aka.doubaocdn.com/s/QQJCmSZPyi",
    "estate":     "https://aka.doubaocdn.com/s/Ux65PUSltd",
    "antique":    "https://aka.doubaocdn.com/s/RDExqVSrh0",
    "jewelry":    "https://aka.doubaocdn.com/s/tIyYtHZat0",
    "wine-tea":   "https://aka.doubaocdn.com/s/joBsBFZknw",
    "timber":     "https://aka.doubaocdn.com/s/VjSud60suu",
    "watch":      "https://aka.doubaocdn.com/s/tgURokyndx",
    "instrument": "https://aka.doubaocdn.com/s/ntBa8zYP8m",
    "coin":       "https://aka.doubaocdn.com/s/H9ki4fthNo",
}
ok = True
try:
    from PIL import Image
except Exception as e:
    print("NO_PIL:", e); ok = False
for name, url in imgs.items():
    jpg = os.path.join(IMG, name + ".jpg")
    webp = os.path.join(IMG, name + ".webp")
    try:
        urllib.request.urlretrieve(url, jpg)
    except Exception as e:
        print("DL_FAIL", name, e); continue
    if ok:
        try:
            im = Image.open(jpg).convert("RGB")
            im.save(webp, "WEBP", quality=82)
            print("OK", name, "webp", os.path.getsize(webp))
        except Exception as e:
            print("CONV_FAIL", name, e)
    else:
        print("KEPT_JPG", name, os.path.getsize(jpg))
print("DONE")
