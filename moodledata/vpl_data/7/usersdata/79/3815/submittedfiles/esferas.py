# -*- coding: utf-8 -*-
from __future__ import division

#Entrado

a = float(input('Peso da bola "A": '))
b = float(input('Peso da bola "B": '))
c = float(input('Peso da bola "C": '))
d = float(input('Peso da bola "D": '))

#Processamento e Saída

if (a == b + c + d) and (b + c == d) and (b == c):
    print('S')
    
else:
    print('N')
    