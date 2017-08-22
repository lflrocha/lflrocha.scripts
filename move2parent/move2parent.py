#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import shutil


diretorio = "/Users/lflrocha/Downloads/_Torrents/Filmes/"
os.system('find ' + diretorio + ' -name .DS_Store -delete')

files = [f for f in os.listdir(diretorio) if os.path.isdir(diretorio+f)]

for name in files:
    dir2 = diretorio + name + '/'
    files2 = [f for f in os.listdir(dir2) if os.path.isfile(dir2+f)]
    print dir2, files2
    for name2 in files2:
        src = diretorio + name + '/' + name2
        #src = src.replace(' ', '\ ')
        #dst = diretorio.replace(' ', '\ ')

        shutil.move(src, diretorio)
