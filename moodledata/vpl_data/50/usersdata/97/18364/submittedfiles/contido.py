# -*- coding: utf-8 -*-
from __future__ import division
def contido(a,b):
    cont=0
    for i in range(0,len(lista),1):
        if b[i] in a:
            cont=cont+1
    return cont
    
a=[]
b=[]
n=input('digite o valor de n:')
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
for i in range(0,n,1):
    b.append(input('digite um elemento:'))

print contido
