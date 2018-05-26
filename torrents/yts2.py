#!/usr/bin/python

import os
import shutil

def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.

Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.

"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename



diretorio = '/Volumes/Leminski/Repositorios/lflrocha.scripts/torrents/'

os.system('find ' + diretorio.replace(' ', '\ ') + ' -name .DS_Store -delete');
os.system('find ' + diretorio.replace(' ', '\ ') + ' -name ._* -delete');

notas = os.listdir(diretorio+'Nota/')

for nota in notas:
    filmes = os.listdir(diretorio+'Nota/'+nota)
    for filme in filmes:
        ano = filme[:4]
        if not os.path.exists(diretorio+'Ano/'+ano):
            print 'cria', ano
            os.mkdir(diretorio+'Ano/'+ano)
        origem = diretorio+'Nota/'+nota+'/'+filme
        destino = diretorio+'Ano/'+ano+'/'+nota+'-'+filme
        #print origem, destino
        shutil.copy(origem, destino)
