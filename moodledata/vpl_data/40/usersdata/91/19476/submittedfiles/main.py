# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return fatorial(n)
    
def valorabsoluto(x):
    if x<0:
        x=x*(-1)
    return x
    
def pi(m):
    soma=0
    j=2
    for i in range(1,m+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2
    soma=soma+3
    return soma
m=input('digite o valor de m:')
a=pi(m)
print('%.15f'%a)
