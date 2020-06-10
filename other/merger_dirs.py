# -*- coding: utf-8 -*-

'''
和并多个文件夹的内容到指定文件夹
'''

import os
import shutil
import sys
from getopt import getopt

def moveAll(dir, new_dir):
    assert os.path.isdir(dir), 'dir is not a directory'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    i=0
    for root, subdir, files in os.walk(dir):
        for file in files:
            i += 1
            old_path = os.path.join(root, file)
            new_path = os.path.join(new_dir, file)
            shutil.copy(old_path, new_path)
            os.remove(old_path)
            print(f'移动{old_path}中...')
    print(i,'个文件被移动')

if __name__ == '__main__':
    args = sys.argv
    helpstr = "use merger_dirs.py -f <from rootdir> -o <output dir> --help"
    try:
        opts, args = getopt(args[1:], "f:o:h", ["help"])
    except getopt.GetoptError:
        print("Error: %s" % helpstr)
    for opt, arg in opts:
        if opt in ("-f"):
            fromdir = arg
        elif opt in ("-o"):
            outdir = arg
        elif opt in ("-h", "--help"):
            print(helpstr)
            exit()
    moveAll(fromdir, outdir)
