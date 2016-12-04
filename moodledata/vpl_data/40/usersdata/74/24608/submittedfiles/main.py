# -*- coding: utf-8 -*-
from __future__ import division
import funcoes


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
        
def cosseno(e,x):
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
        
x = input('Digite o número de x termos da fórmula de pi: ')
y = input('Digite o epsilon para cálculo da razão aurea: ')

z = pii(x)/5

aurea = 2*cosseno(y,z)

print pii(x)
print aurea