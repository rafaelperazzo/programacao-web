# -*- coding: utf-8 -*-
from __future__ import division
def contido(a,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont=cont+1
    return cont
    
a=[]
b=[]
n=input('digite o número de elementos de a:')
m=input('digite o número de elementos de b:')
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
for i in range(0,m,1):
    b.append(input('digite um elemento:'))

print contido(a,b)
