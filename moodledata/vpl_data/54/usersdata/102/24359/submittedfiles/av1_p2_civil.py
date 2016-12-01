# -*- coding: utf-8 -*-
from __future__ import division

def maiorpino(a):
    maiorpino=a[0]
    for i in range(0,len(a),1):
        if a[i]>maiorpino:
            maiorpino=a[i]
    return maiorpino
    
def menorpino(a):
    menorpino=a[0]
    for i in range(0,len(a),1):
        if a[i]<menorpino:
            menorpino=a[i]
    return menorpino

def altura(a,M):
    soma=absoluto(maiorpino(a)-M)+absoluto(menorpino(a)-M)
    return soma

def absoluto(k):
    if k<0:
        k=k*(-1)
        return k
    else:
        return k
        
        
N=int(input('digite o valor de numero de pinos N:'))
M=int(input('digite o valor da altura M:'))
lista=[]
for i in range(0,n,1):
    lista.append(input('digite um elemento da lista:'))

print('%.1d'%(altura(lista,M)))


