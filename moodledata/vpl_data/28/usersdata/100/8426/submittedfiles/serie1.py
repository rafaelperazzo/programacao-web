# -*- coding: utf-8 -*-
from __future__ import division
import math
n = input ('digite o valor de n:')
soma = 0
for i in range (2,n+1,1):
    b = (i- (i-1)) /((i**2)-i)
    if b%2==0:
        soma = soma-b
    else:
        soma = soma+b
print ('%.5f'%soma)