# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Tamanho do lado do quadrado: ')
x1 = input('Coordenada x do primeiro ponto: ')
y1 = input('Coordenada y do primeiro ponto: ')
x2 = input('Coordenada x do segundo ponto: ')
y2 = input('Coordenada y do segundo ponto: ')

s = n/2

if x1<=s and y1<=s or x2>=s or y2>=s:
    print('S')
elif x2<=s and y2<=s or x1>=s or y1>=s:
    print('S')
else:
    print('N')
    
    
