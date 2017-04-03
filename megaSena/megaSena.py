import random


print "Jogos de 8:"
for a in range(1,6):
    print "Jogo ", a
    b = random.sample(range(1, 60), 8)
    c = sorted(b)
    print c
    print ""