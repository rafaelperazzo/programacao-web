# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite n: ')
L=[]

for i in range(0,n,1):
    L.append(input('Digite o valor: '))
soma= L[1]
for i in range(1,n,1):
    soma = soma+ L[i]
ma = soma/n

print L[0]
print L[n-1]
print ma
print L