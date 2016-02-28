# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont
import glob, os

def draw_image(num,file_path):
    print file_path
    file_name, ext=os.path.splitext(file_path)
    im = Image.open(file_path)
    w,h = im.size
    font = ImageFont.truetype('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf', h/5)
    draw = ImageDraw.Draw(im)
    draw.text((w-h/5+5,5),str(num),font=font, fill='red' )
    im.save(file_name+'_with_num.jpg', 'JPEG')

def insert_num(num=0,path=None):
    num = int(num)
    if path is None or len(path)==0:
        for pic in glob.glob('*.jpg'):
            draw_image(num,pic)
    else:
        draw_image(num,path)
    print "Finish!"
    return
if __name__=='__main__':
    num=raw_input('请输入数字（默认为０）：')
    path=raw_input('请输入选择图片（默认为当前路径下jpg）：')
    insert_num(num,path)
