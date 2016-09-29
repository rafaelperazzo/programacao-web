# -*- coding: utf-8 -*-
from __future__ import division
import math
#E
a = input('Digite valor a: ')
b = input('Digite valor b: ')
c = input('Digite valor c: ')
d = input('Digite valor d: ')
contador = 0
#SP
if a>b:
    contador = contador + 1
if a<b and c>d:
    contador = contador + 1
if c>b and c>d:
    contador = contador + 1
if d>c:
    contador = contador + 1
    
if contador == 1:
    print("'S'")
    
else:
       print("'N'")
