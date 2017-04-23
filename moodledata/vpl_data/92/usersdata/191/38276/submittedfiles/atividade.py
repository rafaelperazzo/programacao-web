# -*- coding: utf-8 -*-
import math
n=int(input('valor de n:'))
if n<0:
    n=(-1)*n
soma=0
termo=1
numerador=1
denominador=n
numerador=1
while termo<=n:
    soma=soma+numerador/denominador
    termo=termo+1
    numerador=numerador+1
    denominador=denominador-1
print('%.5f'%soma)


