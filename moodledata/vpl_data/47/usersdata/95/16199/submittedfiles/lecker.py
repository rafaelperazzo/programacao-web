# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont+=1
        elif lista[len(lista)-1]>lista[len(lista)-2]:
            cont+=1
        else lista[i]>lista[i+1] and lista[i]>lista[i-1]:
            cont+=1
    if cont==1:
        return true
    else:
        return false

n=input('n:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('a:'))
for i in range(0,n,1):
    b.append(input('b:'))

if lecker(lista):
    print('S')
else:
    print('N')
