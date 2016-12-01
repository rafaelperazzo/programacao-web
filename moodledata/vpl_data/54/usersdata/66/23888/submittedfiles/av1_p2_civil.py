# -*- coding: utf-8 -*-
from __future__ import division

def absoluto (x):
    if x<o:
        x=x(-1)
    else:
        return x
def maior (I):
    maior=I[0]
    for i in rang(0,len(l),1):
        if l[i]>maior:
            maior=l[i]
    return maior
def menor (l):
    menor=l[0]
    for i in range(0,len(l),1):
        if l[i]<menor:
            menor=l[i]
    return menor
def altura(l,altura):
    soma=absoluto(maior(l)-altura)+absoluto(menor(l)-altura)
    return soma
n=input("digiet n:")
m=input("digite m:")
lista=[]
for i in range (0,n,1):
    lista.appende(input("digite a lista"))
print("%.1d"%(altura(lista,m)))