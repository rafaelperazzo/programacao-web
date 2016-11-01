# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n = input('Digite n: ')

L=[]

for i in range(0,n,1):
    L.append(input('Digite o valor: '))
soma= L[0]

for i in range(1,n,1):
    soma = soma+ L[i]
ma = soma/n

som=0
for j in range (0,n,1):
    som= som +(L[j] - ma) **2
dp=((1/(n-1))*som)**0.5

print ('%.2f' %L[0])
print ('%.2f' %L[n-1])
print ('%.2f' %ma)
print ('%.2f' %dp)
