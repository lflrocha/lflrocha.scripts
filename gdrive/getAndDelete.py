#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os



a = os.system('gdrive list --no-header -m 500 > lista.txt');

with open('lista.txt','r') as f:
    lista = f.read()

aux = lista.split('\n')
for item in aux:
    aux2 = item[:28]
    if len(aux2) > 1:
        os.system('gdrive delete ' + aux2);
