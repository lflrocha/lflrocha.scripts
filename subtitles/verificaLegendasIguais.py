#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import hashlib

diretorio = u'/Volumes/LFLR-HD03/_Organizar/'
diretorio = u'/Users/lflrocha/Desktop/legendas/'

os.system('find ' + diretorio + ' -name .DS_Store -delete')
os.system('find ' + diretorio + ' -name ._* -delete')
os.system('find ' + diretorio + ' -name __MACOSX -delete')
os.system('find ' + diretorio + ' -name Legendas.tv.txt -delete')

lista = []

dirList = os.listdir(diretorio)

for subDir in dirList:    
    lista = []
    subDiretorio = os.listdir(diretorio+subDir)    

    print "\n" + subDir

    for subSub in subDiretorio:

        arquivos = [f for f in os.listdir(diretorio+subDir+'/'+subSub) if f.endswith('.srt')]

        for arq in arquivos:
            
            f = open(diretorio+subDir+'/'+subSub+'/'+arq)
            c = f.read()
            f.close()
            hash_object = hashlib.md5(c)
            f_hash = hash_object.hexdigest()
            print f_hash
            if f_hash not in lista:
                lista.append(f_hash)
                os.rename(diretorio+subDir+'/'+subSub+'/'+arq, diretorio+subDir+'/'+f_hash+arq)
            else:
                print "Removido"
                os.remove(diretorio+subDir+'/'+subSub+'/'+arq)
            
            
os.system('find ' + diretorio + ' -type d -empty -delete')
            