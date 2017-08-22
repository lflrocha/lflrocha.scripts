#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
from mutagen.id3 import TIT2, TALB, TPE1, TDRC, TRCK, TPOS, APIC
from mutagen.mp3 import MP3

import threading

class AsyncID3(threading.Thread):

    def __init__(self, mp3Arquivo, capaArquivo, strTitulo, strAlbum, strBanda, strAno, strTrack, strTotal, strNumAlbum, strTotalAlbum):
        threading.Thread.__init__(self)
        self.mp3Arquivo = mp3Arquivo
        self.capaArquivo = capaArquivo
        self.strTitulo = strTitulo
        self.strAlbum = strAlbum
        self.strBanda = strBanda
        self.strAno = strAno
        self.strTrack = strTrack
        self.strTotal = strTotal
        self.strNumAlbum = strNumAlbum
        self.strTotalAlbum = strTotalAlbum

    def run(self):
        audio = MP3(mp3Arquivo)

        capaMp3 = ''
        if not capaArquivo:
            try:
                capaMp3 = audio.tags['APIC:'].data
            except:
                pass

        audio.delete()
        audio["TIT2"] = TIT2(encoding=3, text=unicode(strTitulo) )
        audio["TALB"] = TALB(encoding=3, text=unicode(strAlbum) )
        audio["TPE1"] = TPE1(encoding=3, text=unicode(strBanda) )
        audio["TDRC"] = TDRC(encoding=3, text=unicode(strAno))
        audio["TRCK"] = TRCK(encoding=3, text=unicode(strTrack+'/'+strTotal))
        audio["TPOS"] = TPOS(encoding=3, text=unicode(strNumAlbum+'/'+strTotalAlbum))
        if capaArquivo or capaMp3:
            imagedata = capaArquivo or capaMp3
            audio["APIC"] = APIC(encoding=3, mime='image/jpg', type=3, desc='', data=imagedata)
        audio.save()

        print 'Arquivo finalizado: ', self.mp3Arquivo



diretorio = u'/Volumes/Leminski/Musica/Musica/_#'

os.system('find ' + diretorio + ' -name .DS_Store -delete');
os.system('find ' + diretorio + ' -name ._* -delete');

dirList = os.listdir(diretorio)

numBandas = len(dirList)

strBanda = ''
strAlbum = ''
strTitulo = ''
strTrack = ''
strTotal = ''
strAno = ''
strNumAlbum = ''
strTotalAlbum = '0'

for banda in dirList:

    subDirList = os.listdir(diretorio+banda+'/')
    numAlbuns = len(subDirList)

    strBanda = banda

    print '\n================================================================='
    print 'Banda: ' + strBanda

    for album in subDirList:

        subSubDirList = [f for f in os.listdir(diretorio+banda+'/'+album+'/') if f.endswith('.mp3')]
        numMusicas = len(subSubDirList)

        strNumAlbum = '1'
        strTotalAlbum = '1'
        aux = album
        aux2 = aux.split('] ')[0]
        strAno = aux2[1:]

        strAlbum = aux.split('] ')[1]
        strTotal = str(numMusicas)
        strTotalLista = {}

        print '\nAlbum: ' + strAlbum + ' - Ano: '+ strAno

        # Número de discos
        for musica in subSubDirList:
            if musica[1] == '-':
                if musica[0] > strTotalAlbum:
                    strTotalAlbum = musica[0]

        # Número de faixas de cada disco
        if musica[1] == '-':
            for musica in subSubDirList:
                l = musica[0]
                if l in strTotalLista.keys():
                    strTotalLista[l] = strTotalLista[l] + 1
                else:
                    strTotalLista[l] = 1

        # Capa
        capaArquivo = ''
        try:
            capaArquivo = open(diretorio+banda+'/'+album+'/capa.jpg', 'rb').read()
        except:
            pass

        for musica in subSubDirList:
            strTrack = musica.split(' ', 1)[0]
            if musica[1] == '-':
                strNumAlbum = musica[0]
                strTrack = strTrack[2:]
                strTotal = unicode(strTotalLista[strNumAlbum])
            aux = musica.split(' ', 1)[1]
            strTitulo = aux.split('.mp3')[0]

            print strTrack + '/' + strTotal + ' - ' + strNumAlbum + '/' + strTotalAlbum + ' - ' + strTitulo

            mp3Arquivo = diretorio+banda+'/'+album+'/'+musica

            background = AsyncID3(mp3Arquivo, capaArquivo, strTitulo, strAlbum, strBanda, strAno, strTrack, strTotal, strNumAlbum, strTotalAlbum)
            background.start()
#            print 'The main program continues to run in foreground.'

        background.join()    # Wait for the background task to finish
#        print 'Main program waited until background was done.'
