# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input (' digite o primeiro valor:' )
b = input (' digite o segundo valor:' )
c = input (' digite o terceiro valor: ')
d = input (' digite o quarto valor: ')

contador = 0

if a>b:
    contador = contador + 1
if a<b>c:
    contador = contador + 1
if b<c>d:
    contador = contador + 1
if d>c:
    contador = contador +1
if contador == 1:
    print ('S')
else: 
    print ('N')