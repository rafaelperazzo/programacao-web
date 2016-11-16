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
    for j in range(0,n,1):
        if a[i]==b[j]:
            cont+=1
print cont
