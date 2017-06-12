# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return true
    else:
        return false
n=int(input('digite n: '))
lista1=[]
lista2=[]
for i in range(0,n,1):
    n1=int(input('digite para lista 1: '))
    lista1.append(n1)
for i in range(0,n,1):
    n2=int(input('digite para lista 2: '))
    lista2.append(n2)
if lecker(lista1):
    print('S')
else:
    print('N')
if lecker(lista2):
    print('S')
else:
    print('N')


                
            