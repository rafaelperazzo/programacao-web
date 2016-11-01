# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('quantidade de valores:')
l=[]
soma=0
for i in range (0,n,1):
    l.append(input('digite o elemento:'))
for j in range (0,n,1):
    soma=soma+l[j]
media=soma/n

soma2=0
for m in range (0,n,1):
    p=(l[m]-media)**2
    soma2=soma2+p
s=(soma2/(n-1))**0.5


print ('%.2f'%l[0])
print ('%.2f'%l[n-1])    
print ('%.2f'%media)
print ('%.2f'%s)
