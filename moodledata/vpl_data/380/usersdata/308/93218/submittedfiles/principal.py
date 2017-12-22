# -*- coding: utf-8 -*-
from minha_bib import *
from random import randint

notas = [0, 0, 0, 0, 0]
for i in range(0, 5):
    x = randint(0, 100)/10.0
    notas.append(x)
    print('Valor sorteado: %.1f' % x)
    print (notas)

for i in range (len(notas), 0, -1):
    print(notas[i-1])
        
    