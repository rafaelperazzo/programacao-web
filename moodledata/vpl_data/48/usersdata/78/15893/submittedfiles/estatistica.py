# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

a=[]
b=[]
n=input('digite o valor de n:')

for i in range (0,n,1):
    a.append(input('digite os elementos da lista:'))

for i in range (0,n,1):
    b.append(input('digite os elementos da lista:'))
    