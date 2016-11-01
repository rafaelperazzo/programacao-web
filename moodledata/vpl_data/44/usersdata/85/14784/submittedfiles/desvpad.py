# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input('Digite o valor de n: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite o número: '))
s=0
for i in range(0,n,1):
    s=s+a[i]
m= s/n
d=0
for i in range(0,n,1):
    d=d+((a[i]-m)**2)
dp=(d/(n-1))**0.5
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%m)
print('%.2f'%dp)