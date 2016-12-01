# -*- coding: utf-8 -*-
from __future__ import division

def modulo(a):
    if a<0:
        a=a*(-1)
    return a
    
def menor(lista):
    t=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]<t:
            t=lista[i]
    return t
    
def maior(lista):
    t=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]>t:
            t=lista[i]
    return t

def movimento(lista,m):
    a=modulo((menor(lista)-m))
    b=modulo((maior(lista)-m))
    total=a+b
    return total
    
n=input('Digite a quantidade de pinos:')
m=input('Digite a altura:')
a=[]

for i in range(0,n,1):
    a.append(input('Digite um valor para n:'))
    
print movimento(a,m)