# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite n: '))
lista1=[]
lista2=[]
for i in range (1,n+1,1):
    n1=int(input('digite valor da lista 1: '))
    n2=int(input('digite valor da lista 2: '))
    lista1.append(n1)
    lista2.append(n2)
cont1=0
cont2=0
for i in range (1,n+1,1):
    if lista1[0]>lista1[1]:
        cont1=cont1+1
    if lista1[n]>lista1[n-1]:
        cont1=cont1+1
    if lista1[i-1]<lista1[i] and lista1[i]>lista1[i+1]:
        cont1=cont1+1
for i in range (1,n+1,1):
    if lista2[0]>lista2[1]:
        cont2=cont2+1
    if lista2[n]>lista2[n-1]:
        cont2=cont2+1
    if lista2[i-1]<lista2[i] and lista2[i]>lista2[i+1]:
        cont2=cont2+1
if cont1>0:
    print('S')
else:
    print('N')
if cont2>0:
    print('N')
else:
    print('N')