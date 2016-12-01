# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np 

def absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x

def altura_maior(l):
    maior=l[0]
    for i in range(0, len(l),1):
        if l[i]>maior:
            maior=l[i]
    return maior
    
def altura_menor(l):
    menor=l[0]
    for i in range(0, len(l),1):
        if l[i]<menor:
            menor=l[i]
    return menor
    
def soma_maior_menor(l,m):
    soma= absoluto(maior(l)-m)+absoluto(menor(l)-m)
    return soma
    
    
n=input('digite o valor de n:')
m=input('digite o valor de m:')
l=[]
a=np.zeros((n,n))
for i in range(0,n,1):
    a.append(input('Digite os elementos da lista: '))
        
print soma_maior_menor(a,m)