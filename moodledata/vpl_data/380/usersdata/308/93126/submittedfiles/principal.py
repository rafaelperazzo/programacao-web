# -*- coding: utf-8 -*-
from minha_bib import *
from random import randint

notas = []
for i in range(0, 5):
    x = randint(0, 100)/10
    notas.append(x)
    print('Valor sorteado: %d' % x)

for i in range (len(notas), -1, -1):
    print(notas[i])
        
    