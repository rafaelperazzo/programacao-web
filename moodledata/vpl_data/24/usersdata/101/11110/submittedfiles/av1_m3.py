# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input ('digite o valor de m: ')

produto = 1
i = 2
j = 3
k = 4
soma = 0
for i in range (1, m+1, 1):
    if m%2==0:
        pi = 3 + (-4/(i*j*k))
    
    else:    
        pi = 3 + (4/(i*j*k))
    soma = soma + pi
    i = i+2
    j = j +2
    k = k+2
    
    print ('%.6f' %pi)
    