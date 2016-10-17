# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input ('digite o valor de m: ')

f = 2
j = 3
k = 4

for i in range (1, m+1, 2):
    if m%2==0:
        soma = soma + (-4/(f*j*k))

    else:    
        soma = soma + (4/(f*j*k))
    
    f = f+2
    j = j+2
    k = k+2
    
    soma = soma + 3
    print ('%.6f' %soma)
    