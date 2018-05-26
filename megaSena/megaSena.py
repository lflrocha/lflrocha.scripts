import random


print "Jogos de 6:"
for a in range(1,6):
    print "Jogo ", a
    b = random.sample(range(1, 60), 6)
    c = sorted(b)
    print c
    print ""

print "Jogos de 7:"
for a in range(1,4):
    print "Jogo ", a
    b = random.sample(range(1, 60), 7)
    c = sorted(b)
    print c
    print ""
