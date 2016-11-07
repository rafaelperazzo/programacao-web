# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n:')
l=[]
for i in range (0,n,1):
    l.append(input('Digite um elemento:'))
    
qntp=0
qnti=0
somai=0
somap=0

for i in range (0,n,1):
    if l[i]%2==1:
        somai=somai+l[i]
print somai

for i in range (0,n,1):
    if l[i]%2==0:
        somap=somap+l[i]
print somap
    