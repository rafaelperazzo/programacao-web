# -*- coding: utf-8 -*-
from __future__ import division

n=input('Quantidade de elementos de a:')
m=input('Quantidade de elementos de b:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('a:'))
for i in range(0,m,1):
    b.append(input('b:'))
    
cont=0
for i in range(0,m,1):
    c=a[i]
    for i in range(0,n,1):
        if c==b[i]:
            cont+=1
print cont

print g