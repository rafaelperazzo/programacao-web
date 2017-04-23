# -*- coding: utf-8 -*-
import math
x=float(input('X:'))
if x<0:
    x=(-1)*x
soma=0
termo=1
denominador=x
numerador=1
while termo<=x:
    soma=soma+numerador/denominador
    termo=termo+1
    numerador=numerador+1
    denominador=denominador-1
print('%.5f'%soma)


