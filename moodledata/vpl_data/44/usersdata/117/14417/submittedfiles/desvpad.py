# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=input('digite a quantidade de números da lisa:')
a=[]

print ('%.2f'%a[0])
print ('%.2f'%a[n-1])

for i in range (0,n,1):
    a.append(input('digite o elemento:'))
    media=media+a[i]
m=media/(len(a))
print ('%.2f'%m)

des=0
for i in range (1,n+1,1):
    des=((a[i]-media**2)+des

des=des*(1/(n-1)
des=des**(1/2)
    
print ('%.2f'%des)