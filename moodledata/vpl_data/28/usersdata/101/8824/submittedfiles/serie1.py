# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('digite o valor de n: ')

soma = 0
sinal = 1
num = 1
den = 1

for i in range (1, n+1, 1):
        soma = soma + sinal*(num/den)
        num = num + 1
        den = num**2
        sinal = - sinal
        
print ( '%.5f' %soma)