#!/usr/bin/python

import os
import os.path
import shutil


diretorio = "/Users/lflrocha/Downloads/_Torrents/Filmes/"

files = [f for f in os.listdir(diretorio) if os.path.isdir(diretorio+f)]

os.system('find ' + diretorio + ' -name .DS_Store -delete')

dst = "/Users/lflrocha/Downloads/_Torrents/Ok/"

for name in files:
    arq = name.rsplit(' - ', 1)
    src = diretorio + name
    dst = diretorio + arq[0]
    print src, dst
    if not os.path.isdir(dst):
        os.mkdir(dst)
    shutil.move(src, dst)
