#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import hashlib
import argparse
from os.path import join, getsize


semanas = [
  'Semana 1: 15 a 24-12-2017',
  'Semana 2: 25-12 a 31-12-2017',
  'Semana 3: 01 a 07-1-2018',
  'Semana 4: 08 a 14-1-2018',
  'Semana 5: 15 a 21-1-2018',
  'Semana 6: 22 a 28-1-2018',
  'Semana 7: 29-1 a 04-2-2018',
  'Semana 8: 05 a 11-2-2018',
  'Semana 9: 12 a 18-2-2018',
  'Semana 10: 19 a 25-2-2018',
  'Semana 11: 26-2 a 4-3-2018',
  'Semana 12: 05 a 11-3-2018',
  'Semana 13: 12 a 18-3-2018',
  'Semana 14: 19 a 25-3-2018',
  'Semana 15: 26-3 a 01-4-2018',
  'Semana 16: 02 a 08-4-2018',
  'Semana 17: 09 a 15-4-2018',
  'Semana 18: 16 a 22-4-2018',
  'Semana 19: 23 a 30-4-2018'
]

tv = [
  'Matérias Factuais',
  'Matérias Especiais',
  'Programas em estúdio',
  'Programas especiais',
  'Programas especiais - Versão reduzida',
  'Programetes temáticos',
  'Programetes temáticos especiais',
  'Flashes ao vivo',
  'Videos educativos',
  'Outros'
]

radio = [
  'Matérias Factuais',
  'Matérias Especiais',
  'Entrevista com especialistas',
  'Programetes educativos',
  'Outros'
]
