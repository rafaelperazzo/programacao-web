# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviop(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio=somatorio+((lista[i]-media)**2)
    resultado=(somatorio/(n-1))**0.5
    return resultado
a=[]
b=[]
n=input('digite a quantidade:')
for i in range (0,n,1):
    a.append(input('digite um elemento:'))
for i in range (0,n,1):
    b.append(input('digite um elemento:'))

media a = media(a)
