# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o numero de elementos:')
a=[]
for i in range (0,n,1):
    a.append(input('Digite o elemento:'))

s=0
for i in range (0,n,1):
    s=s+a[i]
med=s/n
x=0
for i in range (0,n,1):
    x=x+((a[i]-med)**2)
dp=(x/(n-1))**0.5    
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%med)
print('%.2f'%dp)


