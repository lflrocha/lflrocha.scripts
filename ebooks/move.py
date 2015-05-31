import os

for f in os.listdir('./PTBR/'):
    print f
    inicial = f[0]
    for j in os.listdir('./PTBR/'+f):
        print j
        os.rename('./PTBR/'+f+'/'+j,'../_Literatura/'+inicial+'/'+j)