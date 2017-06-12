# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return(V)
    else:
        return(F)
a=[]
n=int(input('digite a quantidade de elementos da lista:'))
for i in range(0,n,1):
    a.append(input('digite um elemento:')