# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite o valor de n:')
soma = 0
for i in range(1,n+1,1):
    t = i / (i**2)
    if i%2==0:
        soma = soma - t
    else:
        soma = soma + t

print('%.5f' %soma)