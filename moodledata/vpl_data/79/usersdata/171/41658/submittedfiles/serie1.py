# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
numerador=1
denominador=numerador**2
for numerador in range(1,n+1,1):
    soma=soma+(numerador/denominador)
    denominador=numerador*numerador
    if numerador%2 !=0:
        numerador=numerador
    else:
        numerador=-numerador
print('%.5f'%soma)
    