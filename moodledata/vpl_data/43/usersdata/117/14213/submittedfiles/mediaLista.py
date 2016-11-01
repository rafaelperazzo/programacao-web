# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de elementos da lista:')
a=[]

for i in range (0,n,1):
    a.append(input('Digite um elemento:'))

print ('%.2f'%a[0])

print('%.2f'%a[n-1])

media=0

for i in range (0,n,1):
    media=media+a[i]

m=media/(len(a))
print ('%.2f'%m)

print (a)