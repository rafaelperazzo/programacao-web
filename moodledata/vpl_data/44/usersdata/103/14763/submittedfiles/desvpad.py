# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite a quantidade de valores da lista:')
a=[]
s=0
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    s=s+a[i]
print ('%.2f'%a[0])
print ('%.2f'%a[n-1])
m=s/(len(a))
print ('%.2f'%m)
print(a)