# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de valores: ')
a=[]
s=0
for i in range (0,n,1):
    a.append(input('Digite o valor: '))
for i in range (0,n,1):
    s=s+a[i]
med=s/n
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print(med)
print(a)
