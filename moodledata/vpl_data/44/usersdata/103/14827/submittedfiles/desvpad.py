# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite a quantidade de valores da lista:')
a=[]
s=0
sx=0
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
    s=s+a[i]
m=s/(len(a))
for k in range (0,n,1):
    x=(a[k]-m)**2
    sx=sx+x
v=((1/(n-1))*sx)**0.5
print ('%.2f'%a[0])
print ('%.2f'%a[n-1])
print ('%.2f'%m)
print(a)
print('%.2f'%v)