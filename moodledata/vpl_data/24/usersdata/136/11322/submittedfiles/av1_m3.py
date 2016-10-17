# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m')

i = 1
soma = 0
j = 2
while i<=m:
    if i%2==0:
        soma = soma - 4/(j)*(j-1)*(j-2)
    else:
        soma = soma + 4/(j)*(j-1)*(j-2)
    j = j+1
    i = i+j
pi = 3 + soma
print('%.5f'%math.pi)