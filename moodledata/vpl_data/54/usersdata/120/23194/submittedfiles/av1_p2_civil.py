# -*- coding: utf-8 -*-
from __future__ import division
def absoluto(x):
    if x<0:
        return x*(-1)
    else:
        return x
def maior(lista):
    i=0
    imaior=0
    while i<len(lista):
        if lista[i]>lista[imaior]:
            imaior=i
        i=i+1
    return imaior     
def menor(lista):
    i=0
    imenor=0
    while i<len(lista):
        if lista[i]<lista[imenor]:
            imenor=i
        i=i+1
    return imenor    
def altura(lista,m):
    soma=(absoluto(maior(lista)-m))+(absoluto(menor(lista)-m))
    
#entrada    
n=input('digite o tamanho da lista:')
m=input('digite o valor da altura:')
a=[]
for i in range(0,n,1):
    a.append(input('digite o elemento da lista:'))

#saida
print altura(a,m)
    