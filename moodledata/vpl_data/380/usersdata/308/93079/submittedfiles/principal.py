# -*- coding: utf-8 -*-
from random import randint
notas = []
n = int(input('Informe a quantidade de notas: '))
for i in range (0, n):
    x = randint(0,100)/10.0
    notas.append(x)
    print('Nota %d sorteada: %.2f' % (i+1, x))

media = 0
for i in notas:
    media += i/float(n)

print('A média das %d notas sorteadas é: %.3f' % (n,media))