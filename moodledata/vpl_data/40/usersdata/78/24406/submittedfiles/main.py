# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
def absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
def fatorial(x):
    fat=1
    for i in range(2,m+1,1):
        fat=fat*(i)
    return fat

def pi(m):
    soma=0
    j=2
    i=0
    while i<=m:
        if i%2==0:
            soma=soma-(4/j*(j+1)*(j+2):
        else:
            soma=soma+(4/(j*(j+1)*(j+2):
        i=i+1
        j=j+2
    pi=3+soma
    return pi
    
def cosseno(z,e):
    soma=0
    i=1
    j=2
    c=(z**a)/fatorial(x)
    while a>e:
        if i%2!=0:
            soma=soma+c
        else:
            soma=soma-c
        i=i+1
        a=a+2
    cosseno=1-soma
    return cosseno
    
def razaoaurea(m,e):
    pi=pi(x)
    cosseno=cosseno(pi/5,e)
    razaoaurea=2*cosseno
    return razaoaurea
        
        
