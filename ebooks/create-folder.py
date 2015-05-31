#!/usr/bin/python

import os
import os.path
import shutil


src = "/Users/lflrocha/_Livros/_Books/__DOC/"

files = os.listdir(src)

for name in files:
    if len(name) > 1:
        srcname = os.path.join(src, name)
        dst = src + str(name[0]).upper()
        dstname = os.path.join(dst, name)
        try:
            os.mkdir(dst)
        except:
            pass
        shutil.move(srcname,dstname)


