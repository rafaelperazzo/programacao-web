# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    i=0
    cont=0
    n=len(lista)
    while i<n:
        if i==0:
            if lista[i]>=lista[i+1]:
                cont=cont+1
        if i==(n-1):
            if lista[n-1]>=lista[n-2]:
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
b=[]
i=0
while i<n:
    elemento=int(input('digite o valor do elemento a ser inserido na lista:'))
    b.append(elemento)
    i=i+1
    if i==n:
        break
if lecker(b):
    print('S')
else:
    print('N')