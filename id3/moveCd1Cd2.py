#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


diretorio = '/Volumes/Leminski/Musica/_Pronto/'

#diretorio = '/Volumes/Leminski/Musica/Organizar/Pink Floyd/'

os.system('find ' + diretorio.replace(' ', '\ ') + ' -name .DS_Store -delete');
os.system('find ' + diretorio.replace(' ', '\ ') + ' -name ._* -delete');

artistas = os.listdir(diretorio)
for artista in artistas:
    discos = os.listdir(diretorio+artista)
    print "Artista", artista
    for disco in discos:
        print "Disco:", disco
        aux = os.listdir(diretorio+artista+'/'+disco)
        for item in aux:
            #print "Item", item
            if item.startswith('CD'):
                print "Moveu"
                musicas = os.listdir(diretorio+artista+'/'+disco+'/'+item)
                numero = item.replace(' ','')[2]
                for musica in musicas:
                    origem = diretorio+artista+'/'+disco+'/'+item+'/'+musica
                    destino = diretorio+artista+'/'+disco+'/'+numero+'-'+musica
                    os.rename(origem, destino)
                    print origem, destino
                os.rmdir(diretorio+artista+'/'+disco+'/'+item)
