# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n= input('Digite um valor: ')
x= []

for i in range(0, n, 1):
    a.append(input('Digite um valor: '))

media=0
for i in range(1, n+1, 1):
    media= media+ a[i]
media= media/n
u= n-1
s0=0
for i in range (0, n-2, 1):
    s0= s0+ (i-media)**(2)
    
s= ((1/n-1)*(s0))**(1/2)

print('%.2f' %a[0])
print('%.2f' %a[u])
print('%.2f' %media)
print('%.2f' %s)
    