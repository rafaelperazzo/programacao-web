# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n:'))
if n<0:
    n=n*(-1)
soma=0
termo=1
numerador=1
denominador=n
while termo<=n:
    soma=soma+numerador/denominador
    termo=termo+1
    numerador=numerador+1
    denominador=denominador-1
print('%.5f'%soma)    


