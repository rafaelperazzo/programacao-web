# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n=input('digite a quantidade de números da lisa:')
a=[]


media=0
for i in range (0,n,1):
    a.append(input('digite o elemento:'))
    media=media+a[i]
m=media/(len(a))

print ('%.2f'%m)
print ('%.2f'%a[0])
print ('%.2f'%a[n-1])

z=0
des=0
for i in range (1,n+1,1):
    des=((a[z]-m)**2)+des
    z=z+1
 

des=des*(1/(n-1))
des=des**(1/2)
    
print ('%.2f'%des)