# -*- coding: utf-8 -*-
import os
import sys
from getopt import getopt
from PIL import Image

'''
提前安装好pillow库或者PIL(PIL已经不维护了)
使用方式: python icon_maker.py -i xx.png -d xxdir
'''

# 所有需要生成的icon宽度
ALL_ICONS = [[20,"20"], [40,"20@2x"], [60, "20@3x"], [29,"29"], [58,"29@2x"],
             [87,"29@3x"], [40,"40"], [80,"40@2x"], [120,"40@3x"], [50,"50"], 
             [100, "50@2x"], [57, "57"], [114, "57@2x"], [120, "60@2x"], [180, "60@3x"], 
             [72,"72"], [144,"72@2x"], [76,"76"], [152, "76@2x"], [167, "83.5@2x"], 
             [1024,"1025"]]

def make_icon(argv):
    helpstr = "use icon_maker.py -i <image file> -d <output dir> --help"
    try:
        opts, args = getopt(argv[1:], "i:d:h", ["help"])
    except getopt.GetoptError:
        print("Error: %s" % helpstr)
    for opt, arg in opts:
        if opt in ("-i"):
            infile = arg
        elif opt in ("-d"):
            outdir = arg
        elif opt in ("-h", "--help"):
            print(helpstr)
            exit()
    if not infile or not outdir:
        print("输入正确的图片路径和导出路径")
        exit()
    # img = Image.open(infile)

    print('infile:' + infile)
    with Image.open(infile) as img:
        (w,h) = img.size
        print('originW:' + str(w) + ',originH:' + str(h))

        for icon in ALL_ICONS:
            newW = icon[0]
            newH = icon[0]
            outfile = os.path.join(outdir, 'Icon-' + icon[1] + '.png')
            out = img.resize((newW,newH),Image.ANTIALIAS) #resize image with high-quality
            out.save(outfile)
            print('output file ' + 'Icon-' + icon[1] + '.png...')
        print('Export all ICONS finished...')
        os.system('open ' + outdir)


if __name__ == "__main__":
    make_icon(sys.argv)