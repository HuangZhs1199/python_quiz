#! /Users/huanghuang/anaconda/bin/python
#-*- coding:utf-8 -*-
from PIL import Image,ImageFont,ImageDraw
import random
import os
img = Image.open("test.jpg")
img.show()
msgFont = ImageFont.truetype('/Library/Fonts/华文仿宋.ttf',18)
msgdraw = ImageDraw.Draw(img)
msgNum = str(random.randint(1,99))
w,h = img.size
wDraw = w*0.85
hDraw = h*0.1
msgdraw.text((wDraw,hDraw),msgNum,font=msgFont,fill=(255,0,0))
img.save('sh_msg.png','png')
img.show()
