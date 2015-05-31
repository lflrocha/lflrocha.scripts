#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os

diretorio = u'/Users/lflrocha/Desktop/bolao/'

fArq = open(diretorio+'quartas.csv'  , 'r')
linhas = fArq.readlines()

fout = open( diretorio+'saida.htm' , 'w')

fout.write('<html>')

fout.write('<head>')
fout.write('<meta charset="utf-8">')
fout.write('<title>Bolão DINES - Mata Mata</title>')
fout.write('<link rel="stylesheet" href="estilos.css">')
fout.write('</head>')

fout.write('<body>')

for linha in linhas[1:]:
    aux = linha.split(',')
    hora = aux[0]
    nome =  aux[1]
    email =  aux[2]

    bra = aux[3]
    col = aux[4]
    fra = aux[5]    
    ale = aux[6]
    hol = aux[7]
    cos = aux[8]
    arg = aux[9]
    bel = aux[10]
    
    fout.write('<p><b>'+nome+'</b><br />')
    fout.write('Brasil '+bra+' x '+col+' Colômbia<br />')
    fout.write('França '+fra+' x '+ale+' Alemanha<br />')
    fout.write('Holanda '+hol+' x '+cos+' Costa Rica<br />')
    fout.write('Argentina '+arg+' x '+bel+' Bélgica<br />')
    fout.write('<br />')

#    fout.write('<p><b>'+nome+'</b><br />')
#    fout.write(bra+'<br>')
#    fout.write(col+'<br>')
#    fout.write(hol+'<br>')
#    fout.write(cos+'<br>')
#    fout.write(fra+'<br>')
#    fout.write(ale+'<br>')
#    fout.write(arg+'<br>')
#    fout.write(bel+'<br>')
#    fout.write('<br />')
#    fout.write(chi+'<br>')
#    fout.write(uru+'<br>')
#    fout.write(mex+'<br>')
#    fout.write(gre+'<br>')
#    fout.write(nig+'<br>')
#    fout.write(alg+'<br>')
#    fout.write(sui+'<br>')
#    fout.write(usa+'<br>')
#    fout.write('<br />')
#    fout.write('<br />')    

#    fout.write('<p><b>'+nome+'</b><br />')


fout.write('</body>')
fout.write('</html>')






