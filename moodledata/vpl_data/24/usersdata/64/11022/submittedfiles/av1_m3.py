# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m: ')

i = 0
j = 0
k = 0
pi = 0
cont = 0

for i in range (0, m+1,1):
    if m%2 == 0:
        pi = pi + (3 + (4/(i*j*k))
    else:
        pi = pi + (3 - (4/(i*j*k)))
        
   
    
print ("%.6f" % pi)