# -*- coding: utf-8 -*-
from __future__ import divisionf 

contador=0
def contido(a,b):
for i in range(0,len(b),1):
    if b[i] in a:
        contador=contador+1
return contador

n=input('digite a quantidade de elementos de a:')
m=input('digite a quantidade de elementos de b:')

a=[]
for i in range(0,n,1):
    a.append(input('digite um elemento:'))

b=[]
for i in range(0,n,1):
    b.append(input('digite um elemento:'))
    
print contido(a,b)
