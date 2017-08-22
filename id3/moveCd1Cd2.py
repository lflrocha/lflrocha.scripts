#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


diretorio = '/Volumes/Leminski/Musica/_OK/REM/'

#diretorio = '/Volumes/Leminski/Musica/Organizar/Pink Floyd/'

os.system('find ' + diretorio.replace(' ', '\ ') + ' -name .DS_Store -delete');
os.system('find ' + diretorio.replace(' ', '\ ') + ' -name ._* -delete');

artista = os.listdir(diretorio)
print "Artista", artista
for disco in artista:
    print "Disco:", disco
    aux = os.listdir(diretorio+disco)
    for item in aux:
        print "Item", item
        if item.startswith('CD'):
            musicas = os.listdir(diretorio+disco+'/'+item)
            numero = item.replace(' ','')[2]
            for musica in musicas:
                origem = diretorio+disco+'/'+item+'/'+musica
                destino = diretorio+disco+'/'+numero+'-'+musica
                os.rename(origem, destino)
                print origem, destino
            os.rmdir(diretorio+disco+'/'+item)
