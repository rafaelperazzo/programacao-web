# -*- coding: utf-8 -*-
from __future__ import division

def maior(a):
    maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return maior
    
def menor(a):
    menor=a[0]
    for i in range(0,len(a),1):
        if a[i]<menor:
            menor=a[i]
    return menor

def altura(a,altura):
    soma=soma(maior(a)-altura)+(menor(a)-altura)
    return soma

def soma(k):
    if k<0:
        k=k*(-1)
        return k
    else:
        return k
        
        
n=input('digite o valor de n:')
m=input('digite o valor de m:')
lista=[]
for i in range(0,n,1):
    lista.append(input('digite um elemento da lista:'))

print('%.1d'%(altura(lista,m)))


