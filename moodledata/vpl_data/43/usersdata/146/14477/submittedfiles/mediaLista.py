# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite n: ')

L=[]

for i in range(0,n,1):
    L.append(input('Digite o valor: '))
soma= L[0]
for i in range(1,n,1):
    soma = soma+ L[i]
ma = soma/n

print ('%.2f' %L[0])
print ('%.2f' %L[n-1])
print ('%.2f' %ma)
print ('%.2f' %L)
