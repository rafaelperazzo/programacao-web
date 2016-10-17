# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input ('digite o valor de m: ')

i = 2
j = 3
k = 4
soma = 0

while i <= m:
    if m%2==0:
        pi = 3 - (4/(i*j*k))

    else:    
        pi = 3 + (4/(i*j*k))
    
    i = i+2
    j = j+2
    k = k+2
    
    print ('%.6f' %pi)
    