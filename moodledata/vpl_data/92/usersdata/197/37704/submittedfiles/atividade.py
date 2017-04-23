# -*- coding: utf-8 -*-
import math
n=int(input('Digite o numéro de termos da série:'))
if n<0:
    n=n*(-1)
soma=0
termo=1
while termo<=n:
    soma=soma+(termo/n)
    termo=termo+1
    n=n-1
print('%.5f'%soma)