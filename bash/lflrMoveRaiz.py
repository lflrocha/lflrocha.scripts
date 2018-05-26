#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import shutil
import argparse


from os.path import join, getsize

parser = argparse.ArgumentParser(description='Descrição do script.')
parser.add_argument('-i','--input', help='Input folder', default='./')
args = parser.parse_args()

diretorio = args.input
os.system('find ' + diretorio + ' -name .DS_Store -delete')

files = [f for f in os.listdir(diretorio) if os.path.isdir(diretorio+f)]

for name in files:
    print name
    dir2 = diretorio + name + '/'
    #print dir2+f
    files2 = [f for f in os.listdir(dir2) if os.path.isdir(dir2+f)]
    #print dir2, files2
    for name2 in files2:
        src = diretorio + name + '/' + name2
        #src = src.replace(' ', '\ ')
        #dst = diretorio.replace(' ', '\ ')
        print src, diretorio
        shutil.move(src, diretorio)
