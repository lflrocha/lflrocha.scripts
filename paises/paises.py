#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import shutil

os.system('find . -name ._* -delete');

with open('country-flags-master/paises.json','r') as data_file:
    paises = json.load(data_file)

#l = paises.keys()
#print len(l), set([x for x in l if l.count(x) > 1])

for x in paises.keys():
    filename1 = './country-flags-master/png1000px/'+x+'.png'
    filename2 = './bandeiras/'+paises[x]+'.png'

#    print filename1, filename2
    shutil.copy (filename1, filename2)
    #os.system(u'echo cp ./country-flags-master/png1000px/'+x+'.png ./bandeiras/'+paises[x]+'.png' )
