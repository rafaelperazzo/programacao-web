# -*- coding: utf-8 -*-
import math
n=int(input('digite o número de termos:'))
if n<0:
    n=n*(-1)
cont=0
soma=0
while cont<=n+1:
    soma=soma+(cont/n)
    cont=cont+1
    n=n-1
print('%.5f'%soma)
    