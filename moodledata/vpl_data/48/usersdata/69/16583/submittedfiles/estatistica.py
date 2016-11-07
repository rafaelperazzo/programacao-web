# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio (lista):
    d=0
    for i in range(0,n,1):
        d=d+((lista[i]- media(lista))**2) 
    resultado=(d/(n-1))**0.5
    return resultado
a=[]
b=[]
n=input ('digite a quantidade de elementos:')
for i in range (0,n,1):
    a.append(input('digite um número:'))
for i in range (0,n,1):
    b.append(input('digite um número:'))
mediaA= media(a)
mediaB=media(b)
desvioA= desvio(a)
desvioB= desvio(b)

