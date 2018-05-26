#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import shutil
import argparse

parser = argparse.ArgumentParser(description='Descrição do script.')
parser.add_argument('-i','--input', help='Input folder', default='./')
parser.add_argument('-o','--output', help='Output folder',required=True)
args = parser.parse_args()

print args.input, args.output
