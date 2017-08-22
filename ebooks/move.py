#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

origem = '/Volumes/Leminski/Livros/'
destino = '/Volumes/Leminski/Google Drive/Livros/ePub/'

os.system('find ' + origem + ' -name .DS_Store -delete');


for f in os.listdir(origem):

    inicial = f[0]
    print inicial, origem+f, destino+inicial+'/'+f

    os.rename(origem+f,destino+inicial+'/'+f)
