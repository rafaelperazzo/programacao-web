# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('digite o valor de n: ')
soma = 0
sinal = 1
N = 1
D = 1

for i in range (1, n+1, 1):
    {
        soma = sinal*(N/D)
        N = N + 1
        D = N**2
        sinal = - sinal
        }
print ( '%.5f' %soma)