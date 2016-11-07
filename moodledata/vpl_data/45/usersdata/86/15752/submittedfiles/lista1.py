# -*- coding: utf-8 -*-
from __future__ import division

n = input('digite n:')
a =[]
for i in range(1,n+1,1):
    a.append(input('digite elemento:'))
conti=0
contp=0
somaim=0
somap=0
for i in range(0,n,1):
    if a[i]%2==1:
        somaim=somaim+a[i]
        conti=conti+1
    if a[i]%2==0:
        somap=somap+a[i]
        contp=contp+1
print(somaim)
print(somap)
print(conti)
print(contp)
print(a)