# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite a quantidade de valores:')
a=[]
for i in range (0,n,1):
    a.append(input('digite um número:'))
s=0
for i in range (0,n,1):
    s=s+a[i]
media=s/n
print('%.2f' %a[0])
print('%.2f' %a[n-1])
print('%.2f' %media)
print(a)

