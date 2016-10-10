# -*- coding: utf-8 -*-
from __future__ import division
import math
n = input ('digite o valor de n:')
soma = 0
for i in range (1, n+1,1):
    b = i/(i**2)
    if (i/i**2)%2==0:
        soma = soma -b
    elif (i/i**2)%2==0:
        soma = soma + b 
print soma