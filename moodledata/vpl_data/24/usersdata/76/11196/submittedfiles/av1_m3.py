# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m:')

i = 2
j = 3
k = 4
soma = 3
cont = 1

while i<=m:

    if cont%2 == 0:
        soma = soma - (4/(i*j*k))
    else:
        soma = soma + (4/(i*j*k))
       
    i = i + 2
    j = j + 2
    k = k + 2
    cont = cont + 2
    
print('%.6f' % soma)