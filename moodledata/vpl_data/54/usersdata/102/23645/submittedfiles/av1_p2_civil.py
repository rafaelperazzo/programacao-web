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

def altura(a,M):
    soma=absoluto(maior(a)-M)+absoluto(menor(a)-M)
    return soma

def absoluto(k):
    if k<0:
        k=k*(-1)
        return k
    else:
        return k
        
        
n=input('digite o valor de n:')
M=input('digite o valor de M:')
l=[]
for i in range(0,n,1):
    l.append(input('digite um elemento da lista:'))

print('%.1d'%(altura(lista,M)))


