# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('digite o valor de n:')
b=[]
for i in range(0,n,1):
    b.append(input('digite um número:'))
s=0
for i in range(0,n,1):
    s=s+[b]
media=s/n
d=0
for i in range(0,n,1):
    d=d+((b[i]-media)**2)
dp=(d/(n-1)**0.5)
print('%.2f'%b[0])
print('%.2f'%b[n-1])
print('%.2f'%media)
print('%.2f'%dp)