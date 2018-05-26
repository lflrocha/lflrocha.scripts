#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import hashlib
import argparse
from os.path import join, getsize

parser = argparse.ArgumentParser(description='Descrição do script.')
parser.add_argument('-i','--input', help='Input folder', default='./')
args = parser.parse_args()

lista = []
d = {}
i = 0
j = 0
for root, dirs, files in os.walk(args.input):
    tamanho = len(files)
    #print tamanho, root
    for idx, name in enumerate(files):
        arq = join(root, name)
        f = open(arq)
        c = f.read()
        f.close()
        hash_object = hashlib.md5(c)
        f_hash = hash_object.hexdigest()
        if f_hash in d.keys():
            os.remove(arq)
            print arq
            #j = j + 1
        else:
            d[f_hash] = [arq]
        #if idx%10 == 0:
            #print str(idx) + "/" + str(tamanho)

print str(j) + " arquivos removidos."
