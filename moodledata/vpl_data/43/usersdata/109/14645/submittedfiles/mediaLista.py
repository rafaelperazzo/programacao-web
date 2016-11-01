# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n:')
a=[]

for i in range (0,n,1):
    a.append(input('Digite um número:'))
    
cont=0
for p in range (0,n,1):
    cont=cont+a[p]
    
print(a[0])
print(a[n])
print(cont)
print(a)