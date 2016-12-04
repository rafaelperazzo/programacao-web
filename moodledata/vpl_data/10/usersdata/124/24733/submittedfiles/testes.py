# -*- coding: utf-8 -*-
from __future__ import division

def vabsol(x):
    if x < 0:
        x = -1*x
    return x

def calculopi(x):
    i = 3
    d = 2
    cont = 0
    for i in range (0,x+1,1):
        if cont%2 != 0:
            i = i - 4/(d*(d+1)*(d+2))
        if cont%2 == 0:
            i = i + 4/(d*(d+1)*(d+2))
        cont = cont + 1
        d = d + 2
    return i
    
print calculopi(1)