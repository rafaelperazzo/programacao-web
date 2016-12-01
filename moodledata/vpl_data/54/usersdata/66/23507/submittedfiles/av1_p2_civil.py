# -*- coding: utf-8 -*-
from __future__ import division

def absoluto (x):
    if x<o:
        x=x(-1)
    else:
        return x
def maior (I):
    maior=I[0]
    for i in rang(0,len((I),1):
        if I[i]>maior:
            maior=I[i]
    return maior
def menor (I):
    menor=I[0]
    for i in range(0,len(I),1):
        if I[i]<menor:
            menor=I[i]
    return menor
def altura(I,altura):
    soma=absoluto(maior(I)-altura)+absoluto(menor(I)-altura)
    return soma
n=input("digiet n:")
m=input("digite m:")
lista=[]
for i in range (0,n,1):
    lista.appende(input("digite a lista"))
print("%.1d"%(altura(lista,m)))