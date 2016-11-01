# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n = input('digite n:')
a=[]
soma=0
for i in range(0,n,1):
    a.append(input('digite o item:'))
    soma=soma+a[i]
media=soma/n
c=0
for k in range(0,n,1):
    j=(k-media)**2
    c=c+j
s=((1/(n-1))*c)**0.5

print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%media)
print('%.2f'%s)
