# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite o valor de n:')
a=[]
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))
print('%.2f'%a[0])
print('%.2f'%a[len(a)-1])
s=0
for i in range(0,n,1):
    s=s+a[i]
s=s/(len(a)) 
print('%.2f'%s)
print(a)