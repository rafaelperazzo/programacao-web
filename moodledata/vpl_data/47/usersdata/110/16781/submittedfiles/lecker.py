# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    if lista[0]>lista[1]:
        cont=cont+1
    if lista[len(lista)-1]>lista[len(lista)-2]:
        cont=cont+1
    for i in range(1,n-1,1):
        if lista[i-1]<lista[i]>lista[i+1]:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
n=input('Digite n: ')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite o elemento:'))
for i in range(0,n,1):
    b.append(input('Digite o elemento: '))
if lecker(a):
    print('S')
else:
    print('N')
if lecker(b):
    print('S')
else:
    print('N')