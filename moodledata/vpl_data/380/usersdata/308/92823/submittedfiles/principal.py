# -*- coding: utf-8 -*-
from random import randint
notas = []
for i in range (0, 50):
    x = randint(1,100)/10
    notas[i].append(x)
    print('Nota adicionada: %.2f' % x)
    
for i in notas:
    media += i/50