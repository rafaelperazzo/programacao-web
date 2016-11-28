# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    a=[]
    cont=0
    for i in range(0,len(lista)-1,1):
        cont= lista[i]-lista[i+1]
        if lista[i+1]>lista[i]:
            cont=a[i+1]-a[i]
        a.insert(0,cont)
    return a

n=input('digite n:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a:'))
c=degrau(a)
print c

