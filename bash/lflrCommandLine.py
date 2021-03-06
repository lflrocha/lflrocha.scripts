#!/usr/bin/python

import os
import os.path
import shutil
import argparse

parser = argparse.ArgumentParser(description='ADD YOUR DESCRIPTION HERE')
parser.add_argument('-o','--output', help='Output folder',required=True)
args = parser.parse_args()

diretorio = os.getcwd()+'/'
os.system('find ' + diretorio + ' -name .DS_Store -delete')

files = [f for f in os.listdir(diretorio) if os.path.isdir(diretorio)]

for name in files:
    ano = name.rsplit('(')
    ano = ano[1]
    ano = ano[:4]
    src = diretorio + name
    dst = args.output + ano + '/'
    print src, dst
    if not os.path.isdir(dst):
        os.mkdir(dst)
    shutil.move(src, dst)
