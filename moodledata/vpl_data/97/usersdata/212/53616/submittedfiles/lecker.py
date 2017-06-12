# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    i=0
    cont=0
    n=len(lista)
    while i<n:
        if i==0:
            if lista[0]>lista[i+1]:
                cont=cont+1
        elif i==(n-1):
            if lista[n-1]>lista[n-2]:
                cont=cont+1
        elif lista[i]>lista[i+1] and lista[i]>lista[i-1]: 
              cont=cont+1
        i=i+1
    if cont==1:
        return(1)
    else:
        return(2)
n=int(input('digite o número de elemententos da lista:'))
a=[]
i=0
while i<n:
    elemento=int(input('digite o valor do elemento a ser inserido na lista:'))
    a.append(elemento)
    i=i+1
    if i==n:
        break
b=[]
i=0
while i<n:
    elemento=int(input('digite o valor do elemento a ser inserido na segunda lista lista:'))
    b.append(elemento)
    i=i+1
    if i==n:
        break
if lecker(a)==1:
    print('S')
else:
    print('N')
if lecker(b)==1:
    print('S')
else:
    print('N')