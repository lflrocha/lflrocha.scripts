#!/usr/bin/python

import os

diretorio = u'/Users/lflrocha/Livros/__Bagunca/ok1/'

os.system('find ' + diretorio + ' -name .DS_Store -delete');


files = [f for f in os.listdir(diretorio) if os.path.isfile(diretorio+f)]


for f in files: 
    print f
    a = f.split('.pdf')
    titulo = a[0]
    
    b = titulo.split(' ')
    
    nome = ""
    for palavra in b:
#        print palavra
        
        if palavra[0] >= "A" and palavra[0] <= "Z":
#            print "maiuscula"
            nome = nome + ' ' + palavra.capitalize() 
        else:
            nome = nome + ' ' + palavra
        
    nome = nome + '.pdf'
    
    os.rename(diretorio+f, diretorio+'ok/'+nome)
            
    
    
    
