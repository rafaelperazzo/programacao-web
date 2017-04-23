# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de termos:'))
denominador=n
numerador=1
termo=0
soma=1
while termo<=n:
    soma=soma+(numerador/denominador)
    numerador=numerador+1
    denominador=n-1
    termo=termo+1
resultado=soma
print('s=%.5f'%resultado)