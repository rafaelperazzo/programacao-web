# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite a quantidade de valores: ')
a=[]
s=0
for i in range (0,n,1):
    a.append(input('Digite o valor: '))
for i in range (0,n,1):
    s=s+a[i]
soma=0
for i in range (0,n,1):
    soma=((a[i]-med)**2)+soma
desviop=((1/(n-1))*soma)**0.5
med=s/n
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%med)
print(a)
print('%.2f'%desviop)