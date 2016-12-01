# -*- coding: utf-8 -*-
from __future__ import division
def abs(x):
    if x<0:
        return x*(-1)
    else:
        return x
        
def maiorI(l):
    maiorI=l[0]
    for i in range(0,len(l),1):
        if l[i]>maiorI:
            maiorI=l[i]
    return maiorI
    
def menorI(l):
    menorI=l[0]
    for i in range(0,len(l),1):
        if l[i]<menorI:
            menorI=l[i]
    return menorI
    
def alt(l,alt):
    soma=abs(maiorI(l)-alt)+abs(menorI(l)-alt))
    return soma
    
n=input('Digite n:')
m=input('Digite a altura:')

lista=[]
for i in range(0,n,1):
    lista.append(input('Digite os elementos da lista'))
    
print ((alt(lista,m)))