# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    a=[]
    cont=0
    for i in range(0,len(lista)-1,1):
        cont= a[i]-a[i-1]
        if a[i+1]>a[i]:
            cont=a[i+1]-a[i]
        a.insert(0,cont)
    return a

n=input('digite n:')
lista=[]
for i in range(0,n,1):
    lista.append(input(digite lista: '))
c=degrau(lista) 
print c

