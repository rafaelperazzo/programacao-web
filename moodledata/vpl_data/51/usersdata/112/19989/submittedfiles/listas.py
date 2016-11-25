# -*- coding: utf-8 -*-
from __future__ import division

a=[]
n=input('Digite a quantidade de componentes da lista:')
for i in range (0,n,1):
    a.append(input('Digite um termo para a lista:'))
def maiordegrau(lista):
    maior=0
    for i in range(0,len(lista),1):
        lista[i]=maior
        if lista[i+1]>maior:
            maior=lista[i+1]
            return lista[i+1]
print maiordegrau(a)
        