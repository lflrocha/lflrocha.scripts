#!/usr/bin/python

import os
import os.path
import shutil


diretorio = "/Users/lflrocha/Downloads/_Torrents/Filmes/"

files = [f for f in os.listdir(diretorio) if os.path.isfile(diretorio+f)]

os.system('find ' + diretorio + ' -name .DS_Store -delete')

dst = "/Users/lflrocha/Downloads/_Torrents/Filmes/"

for name in files:
    src = diretorio + name

    arq = name.rsplit('.', 1)
    arq = arq[0]
    dst = diretorio + arq
    if not os.path.isdir(dst):
        os.mkdir(dst)

    print src, dst
    shutil.move(src, dst)
