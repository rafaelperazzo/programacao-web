# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de termos:'))
if n<=0:
    n*(-1)
soma=0
denominador=n
numerador=1
termo=1
while termo<=n:
    soma=soma+(numerador/denominador)
    numerador=numerador+1
    denominador=n-1
    termo=termo+1
print('%.5f'%soma)