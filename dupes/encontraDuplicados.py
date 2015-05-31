#!/usr/bin/python
# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import urllib
import os
import hashlib
from os.path import join, getsize

lista = []
d = {}
i = 0
j = 0
for root, dirs, files in os.walk("/Users/lflrocha/Livros"):
    tamanho = len(files)
    print root, tamanho
    for idx, name in enumerate(files):
        arq = join(root, name)
        f = open(arq)
        c = f.read()
        f.close()
        hash_object = hashlib.md5(c)
        f_hash = hash_object.hexdigest()
        if f_hash in d.keys():     
            os.remove(arq)
            j = j + 1
        else:
            d[f_hash] = [arq]
        if idx%10 == 0:
            print str(idx) + "/" + str(tamanho)

print str(j) + " arquivos removidos."

    
#           f = open(arq)
#           c = f.read()
#           f.close()
#           hash_object = hashlib.md5(c)
#           f_hash = hash_object.hexdigest()
#           print f_hash
#           if f_hash not in lista:
#               lista.append(f_hash)
#           else:
#               print "Removido"
        #        os.remove(arq)
