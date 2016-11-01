# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('tamanho da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('digite o proximo elemento da lista: '))
s=0
for i in range(0,n,1):
    s=s+a[i]
media=s/n
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%media)
b=0
for i in range(0,n,1):
    b=b+(a[i]-media)**2
b=(b/(n-1))**0.5
print('%.2f'%b)
    
