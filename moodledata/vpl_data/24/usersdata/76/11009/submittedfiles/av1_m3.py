# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m:')

i = 0
j = 0
k = 0
soma = 0
pi = 0

while i<=m:

i = i + 2
j = j + 2
k = k + 2

    if m%2 == 0:
        soma = soma + 3 - 4/(i*j*k)
    else:
        soma = soma + 3 + 4/(i*j*k)
   
    
print('%.6f' % pi)