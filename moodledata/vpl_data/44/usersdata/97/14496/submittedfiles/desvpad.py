# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('digite a quantidade de valores:')
a=[]
cont=0
for i in range (0,n,1):
    a.append(input('digite um valor:'))

for i in range(0,n,1):
    cont = cont + a[i]
m=cont/n

j=0
soma=0
for i in range(0,n,1):
    soma=((a[j]-m)**2)+soma

soma=(soma)*(1/(n-1))
soma=soma**(1/2)

print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%soma)
print('%.2f'%d)
