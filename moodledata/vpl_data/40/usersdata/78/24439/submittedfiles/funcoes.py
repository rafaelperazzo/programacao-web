# -*- coding: utf-8 -*-
from __future__ import division
#ARQUIVO COM SUAS FUNCOES

def absoluto(m):
    if m<0:
        m=m*(-1)
    return m
    
    
def fatorial(m):
    fat=1
    for i in range(2,m+1,1):
        fat=fat*i
    return fat

def calculopi(m):
    soma=0
    j=2
    for i in range(0,m,1):
        if i%2==0:
            soma=soma+(4/(j*(j+1)*(j+2)))
        else:
            soma=soma-(4/(j*(j+1)*(j+2)))
        j=j+2
    pi=3+soma
    return pi
    
def calculocosseno(z,e):
    soma=0
    i=1
    a=2
    c=(z**a)/fatorial(a)
    while c>e:
        c=(z**a)/fatorial(a)
        if i%2!=0:
            soma=soma+c
        else:
            soma=soma-c
        i=i+1
        a=a+2
        c=c+1
    cosseno=1-soma
    return cosseno
    
def calculorazaoaurea(m,e):
    pi=calculopi(m)
    cosseno=calculocosseno(pi/5,e)
    razaoaurea=2*cosseno
    return razaoaurea