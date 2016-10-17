# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input ('Digite o primeiro número:')
b = input ('Digite o segundo número:')
if a>= b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
contador = 0
if maior %menor == 0:
    contador = contador + 1
    print(menor)
else:
    while True:
        if a%b>0:
            MDC = a%b
            a= b
            b = MDC
            contador = contador+1
        elif a%b == 0:
            contador = contador + 1
            print (MDC)
            break
print (contador)