# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input ('digite o valor de m: ')

produto = 1
f = 2
j = 3
k = 4

while m>0:
    if m%2==0:
        pi = 3 + (-4/(f*j*k))
    
    else:    
        pi = 3 + (4/(f*j*k))
    
    i = i+2
    j = j +2
    k = k+2
    
    print ('%.6f' %pi)
    