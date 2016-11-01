# -*- coding: utf-8 -*-
from __future__ import division
n=input('digite a quantidade de valores:')
a=[]
soma=0
for i in range (0,n,1):
    a.append(input('digite um valor:'))
x=(soma+a[i])/n

print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%x)
print(a)



