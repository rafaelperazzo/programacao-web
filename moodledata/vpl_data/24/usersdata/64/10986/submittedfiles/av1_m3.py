# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m: ')

i = 0
j = 0
k = 0
pi = 0
cont = 0

while cont<=m:
    if m%2 == 0:
        pi = pi + (4/(i*j*k))
    
    i = i + 2
    j = j + 2
    k = k + 2
    cont = cont+1
    
    if m%2 != 0:
        pi = pi + (4/(i*j*k))
        
    i = i + 2
    j = j + 2
    k = k + 2
    cont = cont+1
    
print ("%.6f" % pi)