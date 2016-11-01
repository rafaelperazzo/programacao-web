# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('digite a quantidade de termos:')
a=[]
s=0
for i in range(0,n,1):
    a.append(input('digite a nota:'))
    s=s+a[i]
m=s/n
y=(1/n-1)
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%m)
