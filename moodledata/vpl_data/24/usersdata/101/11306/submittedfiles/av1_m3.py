# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input ('digite o valor de m: ')

f = 2
j = 3
k = 4
soma = 0

for i in range (1, m+1, 2):
    if m%2==0:
        soma = (-4/(f*j*k))

    else:    
        soma = (4/(f*j*k))
    
    f = f+2
    j = j+2
    k = k+2
    pi = soma + 3
    
    print ('%.6f' %pi)
    