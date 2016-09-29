# -*- coding: utf-8 -*-
from __future__ import division
import math
a = input("Digite o valor de a:")
b = input("Digite o valor de b:")
c = input("Digite o valor de c:")
d = input("Digite o valor de d:")
contador = 0

if a>b:
    contador = contador + 1
if a<b>c:
    contador = contador + 1
if b<c>d:
    contador = contador + 1
if c<d:
    contador = contador + 1
if contador==1:
    print("S")
else:
    print("N")
    
