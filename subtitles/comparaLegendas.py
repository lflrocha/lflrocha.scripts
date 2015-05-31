#!/usr/bin/python
# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import urllib
import os
import hashlib

lista = {}
diretorio = u'/Users/lflrocha/Desktop/legendas/'    


def limpa_lixos():
    os.system('find ' + diretorio + ' -name .DS_Store -delete')
    os.system('find ' + diretorio + ' -name ._* -delete')
    os.system('find ' + diretorio + ' -name __MACOSX -delete')
    os.system('find ' + diretorio + ' -name Legendas.tv.txt -delete')


def organiza_legendas():
    dirList = os.listdir(diretorio)
    for subDir in dirList:
        lista = []

        arquivos = [f for f in os.listdir(diretorio+subDir+'/') if f.endswith('.srt')]

        for arq in arquivos:

            f = open(diretorio+subDir+'/'+arq)
            c = f.read()
            f.close()
            hash_object = hashlib.md5(c)
            f_hash = hash_object.hexdigest()
            print f_hash
            if f_hash not in lista:
                lista.append(f_hash)
                os.rename(diretorio+subDir+'/'+arq, diretorio+subDir+'/'+arq)
            else:
                print "Removido"
                os.remove(diretorio+subDir+'/'+arq)

    os.system('find ' + diretorio + ' -type d -empty -delete')




def main():

    limpa_lixos()
    organiza_legendas()

if  __name__ =='__main__':main()

