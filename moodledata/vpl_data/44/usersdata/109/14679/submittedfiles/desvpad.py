# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite n:')
a=[]

for i in range (0,n,1):
    a.append(input('Digite um número:'))
    
cont=0
for p in range (0,n,1):
    cont=cont+a[p]
m=cont/n

print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%m)
print(a)