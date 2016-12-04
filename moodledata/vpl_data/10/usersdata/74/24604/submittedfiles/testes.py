# -*- coding: utf-8 -*-
from __future__ import division

def pii(m):
    i = 2
    j = 3
    k = 4
    l = 1
    pi = 3
    while m>=l:
        if l%2 == 0:
            pi = pi-4/(i*j*k)
        else:
            pi = pi+4/(i*j*k)
        i = i+2
        j = j+2
        k = k+2
        l = l+1
    
    return pi
        
def cosseno(e):
    i = 1
    k = 2
    l = 1
    cos = 1
    j = 1
    
    while e<=j:
        q = k
        while k>l:
            q = q*l
            l = l+1
        if i%2 == 0:
            cos = cos+(x**k)/q
        else:
            cos = cos-(x**k)/q
        j = (x**k)/q
        i = i+1
        k = k+2
    
    return cos
        
x = input('Calcular pi: ')
y = input('Calcular cosseno: ')








