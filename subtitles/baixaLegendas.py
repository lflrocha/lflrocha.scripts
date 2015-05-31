#!/usr/bin/python
# -*- coding: UTF-8 -*-

from HTMLParser import HTMLParser
import urllib
import os
import hashlib

lista = {}
diretorio = u'/Users/lflrocha/Desktop/legendas/'    


# Parser de busca
class BuscaParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            att = dict(attrs)

            if 'href' in att:

                if att['href'].startswith('/download/'):
                    aux = att['href'].split('/')
                    filme = aux[3]

                    if filme in lista.keys():
                        lista[filme].append('http://legendas.tv/downloadarquivo/' + aux[2] ,)
                    else:
                        lista[filme] = ['http://legendas.tv/downloadarquivo/' + aux[2] ]



def encontra_legendas(listaFilmes):
    s_url = 'http://legendas.tv/util/carrega_legendas_busca/'

    print "Procurando legenda: "
    for i, filme in enumerate(listaFilmes):
        print i, filme
        parser = BuscaParser()
        f = urllib.urlopen(s_url + filme)
        s = f.read()
        parser.feed(s)
        f.close()



def baixa_legendas():
    # Faz download das legendas
    print "Baixando legendas: " + str(len(lista))
    for i, filme in enumerate(lista.keys()):
        dirList = os.listdir(diretorio)
        if filme not in dirList:
            os.mkdir(diretorio + filme)
        print i, filme, len(lista[filme])
        for legenda in lista[filme]:
            f = urllib.urlopen(legenda)
            s = f.read()
            f.close()
            nome = legenda.split('/')
            try:
                os.mkdir(diretorio + filme + '/' + nome[4] )
            except:
                pass

            arqNome = diretorio + filme + '/' + nome[4] + '/' + nome[4] + '.rar'
            arq = open(arqNome, 'w')
            arq.write(s)
            arq.close()
            ret = os.system('unrar -idq -y x '+ arqNome + ' ' + diretorio + filme + '/' + nome[4] + '/')
            if ret == 2560:
                os.system('unzip -q -o '+ arqNome + ' -d ' + diretorio + filme + '/' + nome[4] + '/')


def limpa_lixos():
    os.system('find ' + diretorio + ' -name .DS_Store -delete')
    os.system('find ' + diretorio + ' -name ._* -delete')
    os.system('find ' + diretorio + ' -name __MACOSX -delete')
    os.system('find ' + diretorio + ' -name Legendas.tv.txt -delete')


def organiza_legendas():
    dirList = os.listdir(diretorio)
    for subDir in dirList:
        lista = []
        subDiretorio = os.listdir(diretorio+subDir)

        print "\n" + subDir

        for subSub in subDiretorio:

            arquivos = [f for f in os.listdir(diretorio+subDir+'/'+subSub) if f.endswith('.srt')]

            for arq in arquivos:

                f = open(diretorio+subDir+'/'+subSub+'/'+arq)
                c = f.read()
                f.close()
                hash_object = hashlib.md5(c)
                f_hash = hash_object.hexdigest()
                print f_hash
                if f_hash not in lista:
                    lista.append(f_hash)
                    os.rename(diretorio+subDir+'/'+subSub+'/'+arq, diretorio+subDir+'/'+f_hash+arq)
                else:
                    print "Removido"
                    os.remove(diretorio+subDir+'/'+subSub+'/'+arq)

    os.system('find ' + diretorio + ' -type d -empty -delete')




def main():

    filmes = [
"13 Eerie",
"A Thousand Times Good Night",
"Abrir Puertas Y Ventanas",
"After Midnight",
"Alfie",
"All About The Benjamins",
"Amities Sinceres",
"Anatomy Of A Love Seen",
"Anna Karenina",
"Ayrton Senna - Beyond the speed of sound",
"Belle Du Seigneur",
"Blanche",
"Camille",
"Canone Inverso",
"Catch-22",
"Chasers",
"Cheyenne Autumn",
"Choke",
"City Hall",
"Copenhagen",
"Doppelganger",
"Enigma",
"Faroeste Caboclo",
"Grace",
"Grand Prix",
"Hard Cash",
"Human Zoo",
"Jackass Number Two",
"Jimmys Hall",
"Korso",
"Le Meraviglie",
"Le Sourire",
"Magic In The Moonlight",
"Max",
"Mc Q",
"Monty Python Live Mostly",
"Morning Star",
"Mr Destiny",
"Muerte En Buenos Aires",
"Murder By Numbers",
"My Favorite Martian",
"Nell",
"Nymphomaniac Vol I",
"Nymphomaniac Vol II",
"Open Windows",
"Reach Me",
"Richard The Lionheart",
"Saving Mr Banks",
"Soldados De Salamina",
"Stealing Beauty",
"Stonehearst Asylum",
"Stretch",
"Teenage Mutant Ninja Turtle",
"The Day the Earth Caught Fire",
"The Foot Fist Way",
"The Good Son",
"The Naked City",
"The Salvation",
"The Trip To Italy",
"The Young and Prodigious T S Spivet",
"Thunderheart",
"Top Secret",
"Un Plan Parfait",
"White Bird in a Blizzard",
"White Fang",
"Winter Sleep",
"Wrong Turn at Tahoe",
    ]

    encontra_legendas(filmes)
    baixa_legendas()
    limpa_lixos()
    organiza_legendas()

if  __name__ =='__main__':main()

