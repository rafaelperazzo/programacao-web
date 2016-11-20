# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

def fatorial(n):
    produto=1
    for i in range(1,n+1,1):
        produto=produto*i
    return produto
    
def valorabsoluto(x):
    if x<0:
        x=x*(-1)
    return x
    
def pi(y):
    soma=0
    j=2
    for i in range(1,y+1,1):
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        j=j+2
    soma=soma+3
    return soma
y=input('digite o valor de y:')
a=pi(y)
print('%.15f'%a)
