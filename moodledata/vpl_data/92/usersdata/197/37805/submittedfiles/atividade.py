# -*- coding: utf-8 -*-
import math
n=int(input('Digite o numéro de termos da série:'))
if n<0:
    n=n*(-1)
soma=0
termo=1
denominador=n
while termo<=n:
    soma=soma+(termo/denominador)
    termo=termo+1
    denominador=denominador-1
print('%.5f'%soma)