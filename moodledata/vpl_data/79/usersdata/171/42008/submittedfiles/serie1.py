# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
soma=0
denominador=1
for numerador in range(1,n+1,1):
    if numerador%2==0:
        numerador=-(numerador)
    else:
        numerador=numerador
    denominador=numerador*numerador
    soma=soma+(numerador/denominador)
print('%.5f'%soma)
    