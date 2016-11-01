# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('digite a quantidade de valores:')
a=[]
soma=0
for i in range (0,n,1):
    a.append(input('digite um valor:'))

for i in range(0,n,1):
    soma = soma + a[i]
m=soma/n

j=0
d=0
for i in range(1,n+1,1):
    d=((a[j]-m)**2)+d
    j=j+1

d=(d)*(1/n-1)
d=d**(1/2)

print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%soma)
print('%.2f'%d)
