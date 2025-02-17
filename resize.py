#!/usr/bin/env python3

# THE REAL ONE IS IN UR BIN

import music_tag, sys, os
from PIL import Image

def resize(filename):
    f = music_tag.load_file(f"{dir}/{filename}")
    art = f['artwork']
    raw_img = art.first.data

    with open('img.jpg', 'wb') as m:
        m.write(raw_img)

    del f['artwork']
    f.remove_tag('artwork')

    img = Image.open('img.jpg')
    if img.height > 640:
        newsize = (500, 500)
        img = img.resize(newsize, resample=0, box=None)
        img.save('img.jpg', 'JPEG')

        with open('img.jpg', 'rb') as img_in:
            f["artwork"] = img_in.read()

        f.save()
    else: print(f"img height is {img.height}, not doing anything!")

if len(sys.argv) == 1:
    print("Please specify a music directory.")
else:
    dir = sys.argv[1]
    n = 1
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".mp3") or filename.endswith(".flac"):
            print(f"resizing file #{n}")
            resize(filename)
            n = n + 1
        else:
            exit

print("\nall done!!")
