# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m:')

i = 0
j = 0
k = 0
pi = 0

while i<=m:

    if m%2 == 0:
        pi = pi + 3 - 4/(i*j*k)
    else:
        pi = pi + 3 + 4/(i*j*k)
       
        i = i + 2
        j = j + 2
        k = k + 2
   
    
print('%.6f' % pi)