# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('digite a quantidade de elementos:')
l=[]

for i in range (0,n,1):
    l.append(input('digite um elemento:'))
    
print('%.2f'%l[0])
print('%.2f'%l[n-1])

soma=0
i=0
while i<n:
    soma=soma+l[i]
    i=i+1
media=soma/n
print('%.2f'%media)

for i in range (0,n,1):
    soma=soma+((l[i]-media)**2)
d=((soma/(n-1))**0.5)
print('%.2f'%d)