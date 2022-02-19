#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : autofenbianlv.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/5/14
from glob import glob
from PIL import Image
import os

img_path = glob("D:/study/Web/untitled/big work-food/image-food/ice/*.jpg")
path_save = "D:/study/Web/untitled/big work-food/image-food/ice"
a = range(0, len(img_path))
i = 0
for file in img_path:
    name = os.path.join(path_save, "%d.jpg" % a[i])
    im = Image.open(file)
    im.thumbnail((247, 150))
    print(im.format, im.size, im.mode)
    im.save(name, 'JPEG')
    i += 1
