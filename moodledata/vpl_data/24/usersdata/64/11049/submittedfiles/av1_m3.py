# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m: ')

i = 1
j = 1
k = 1
pi = 1
cont = 0

for i in range (0, m+1,1):
    if m%2 == 0:
        pi = pi + (4/(i*j*k))
    else:
        pi = pi + (4/(i*j*k))
     
    i = i + 2
    j = j + 2
    k = k+2
    cont = cont + 1
    
print ("%.6f" % pi)