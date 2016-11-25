# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    maior = lista[1]-lista[0]
    for i in range (1,len(lista)-1,1):
        if (lista[i+1]-lista[i])>maior:
            maior = lista[i+1]-lista[i]
    return maior
    
n = input ('Digite a quantidade de termos:')
a =[]
for i in range(0,n,1):
    a.append(input('Digite um número:')
print (degrau(a))