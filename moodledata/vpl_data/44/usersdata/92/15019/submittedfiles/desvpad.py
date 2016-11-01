# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n= input('Digite um valor: ')
x= []

for i in range(0, n, 1):
    x.append(input('Digite um valor: '))

media=0
for i in range(0, n, 1):
    media= media+ x[i]
media= media/n
u= n-1

s0=0
for i in range (0, n-2, 1):
    s0= s0+ (x[i]-media)**(2)

    
s= ((1/(n-1))*(s0))**(1/2)

print('%.2f' %x[0])
print('%.2f' %x[u])
print('%.2f' %media)
print('%.2f' %s)
    