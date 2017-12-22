# -*- coding: utf-8 -*-
from random import randint
notas = []
for i in range (0, 50):
    x = randint(0,100)/10
    notas.append(x)
    print('Nota %d sorteada: %.2f' % (i+1, x))

media = 0
for i in notas:
    media += i/50

print('A média das 50 notas sorteadas é: %.3f' % media)