# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite um número N:')
soma = 0
for i in range (1,n+1,1):
    if i%2==0:
        soma = soma - i/(i**2)
    else:
        soma = soma + i/(i**2)
print('%.5f'%soma)