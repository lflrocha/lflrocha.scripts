#!/usr/bin/python

import os
import shutil


torrentsPath = '/Volumes/Leminski/Repositorios/lflrocha.scripts/torrents/Ano/'
filmesPath = '/Volumes/LFLR-Filmes/Filmes/'

os.system('find ' + torrentsPath.replace(' ', '\ ') + ' -name .DS_Store -delete');
os.system('find ' + torrentsPath.replace(' ', '\ ') + ' -name ._* -delete');

anos = os.listdir(torrentsPath)

vetFilmes = []

for ano in anos:
    torrents = os.listdir(torrentsPath+ano)
    filmes = os.listdir(filmesPath+ano)
    for filme in filmes:
        filme = filme[:-7]
        vetFilmes.append(filme.lower().replace(' ','-').replace(',','').replace("'",'').replace('!','').replace('.',''))

    for torrent in torrents:
        aux = torrent[7:].rsplit('-',2)[0]
        if aux in vetFilmes:
            arq = torrentsPath+ano+'/'+torrent
            os.rename(arq,'/Volumes/Leminski/Repositorios/lflrocha.scripts/torrents/ok/'+torrent)
        else:
            print "nao"
