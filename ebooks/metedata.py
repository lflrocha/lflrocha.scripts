#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

#diretorios = ['A/','B/','C/','D/','E/','F/','G/','H/','I/','J/','K/','L/','M/','N/','O/','P/','R/','S/','T/','U/','V/','W/','Y/','Z/']
#diretorios = ['A/','B/','C/','D/']
#diretorios = ['E/','F/','G/','H/']
#diretorios = ['I/','J/','K/','L/']
#diretorios = ['M/','N/','O/','P/']
diretorios = ['P/','R/','S/',]
#diretorios = ['T/','U/','V/','W/','Y/','Z/']

for diretorio in diretorios:

    dirList = os.listdir('./'+diretorio)
    #dirList = dirList[:2]

    for livro in dirList:
        print livro
        l = livro.replace(' ', '\ ')
        autor = livro.split(' - ')[0]
        titulo = livro.split(' - ')[1]
        titulo = titulo.replace('.epub', '')
        cmd = "/Applications/calibre.app/Contents/MacOS/ebook-meta " + diretorio + l + " -t \"" + titulo + "\" -a \"" + autor +  "\" -k \"\" -l \"pt-BR\" -r \"\" -p \"\"  -d \"1980-01-21\" -c \"\" --isbn \"\" --tags \"\" --author-sort \"\" --title-sort \"\""
        os.system(cmd)

