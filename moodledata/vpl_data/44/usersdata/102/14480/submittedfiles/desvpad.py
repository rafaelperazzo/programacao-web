# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=int(input('digite a quantidade dos valores de n:'))
l=[]
for i in range (0,n,1):
    l.append(input('digite um valor de n:'))
soma=0
for i in range(0,n,1):
    soma=soma+l[i]

media=soma/n

soma=0
for i in range(0,n,1):
    soma=soma+(l[i]-media)**2

s=((1/(n-1))*soma)**(1/2)

print('%.2f'%l[0])
print('%.2f'%l[n-1])
print('%.2f'%lmedia)
print('%.2f'%s)