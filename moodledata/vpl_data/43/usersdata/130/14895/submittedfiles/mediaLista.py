# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite o valor de n:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))
print(a[0])
print(a[len(a)-1]
s=0
for i in range(0,len(a)+1,1):
    s=s+a[i]
    i=i+1
s=s/(len(a)) 
print(s)
print(a)