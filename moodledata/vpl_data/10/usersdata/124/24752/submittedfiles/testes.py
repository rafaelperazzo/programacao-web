# -*- coding: utf-8 -*-
from __future__ import division

def vabsol(x):
    if x < 0:
        x = -1*x
    return x

def calculopi(y):
    c = 3
    d = 2
    for i in range (0, y, 1):
        if i%2 != 0:
            c = c - (4/(d*(d+1)*(d+2)))
        elif i%2 == 0:
            c = c + (4/(d*(d+1)*(d+2)))
        d = d + 2
    return c
    
def cos(z):
    cos z = 1
    v = 2
    fat = 1
    for i in range (v, 0, -1):
        fat = fat*i
    while epsilon 
    return fat
    
print cos(3)