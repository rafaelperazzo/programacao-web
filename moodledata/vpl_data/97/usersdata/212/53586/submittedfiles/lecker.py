# -*- coding: utf-8 -*-
from __future__ import division
def lecker(ista):
    i=0
    cont=0
    while i<len(lista):
        if i==0:
            if lista[i]>=lista[i+1]:
                cont=cont+1
        if i==(len(lista)-1):
            if lista[len(lista)-1]>=lista[len(lista)-2]:
                cont=cont+1
        if lista[i]>=lista[i+1] and lista[i]>=lista[i+1]: 
              cont=cont+1
    if cont>1:
        return(true)
    else:
        return(false)
n=int(input('digite o número de elemententos da lista:'))
a=[]
i=0
while i<n:
    elemento=int(input('digite o valor do elemento a ser inserido na lista:'))
    a.append(elemento)
    i=i+1
if lecker(a):
    print('S')
else:
    print('N')