# -*- coding: utf-8 -*-
from __future__ import division
import math
a = ("Digite o valor de a:")
b = ("Digite o valor de b:")
c = ("Digite o valor de c:")
d = ("Digite o valor de d:")
contador = 0

if a>b:
    contador = contador + 1
if a<b>c:
    contador = contador + 1
if b<c>d:
    contador = contador + 1
if c<d:
    contador = contador + 1
if contador ==1:
    print("S")
else:
    print("N")
    
