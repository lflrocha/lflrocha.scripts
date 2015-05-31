#!/usr/bin/python

import os

diretorio = u'/Users/lflrocha/Livros/PDF/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');

files = [f for f in os.listdir(diretorio) if os.path.isfile(diretorio+f)]

for f in files:
    print f
    a = f.split('.pdf')
#    print a[0].count('-')
    if a[0].count('-') == 1:
        b = a[0].split(' - ')
        if len(b) == 2:
            titulo = b[0]
            autor = b[1]
    
#           c = autor.split(', ')
#           nome = c[1]
#           sobrenome = c[0]    
#           d = nome + ' ' + sobrenome + ' - '+ titulo + '.pdf'

            d = autor + ' - ' + titulo + '.pdf'
            os.rename(diretorio+f, diretorio+'ok/'+d)
            