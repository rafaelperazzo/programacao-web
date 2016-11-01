# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de elementos da lista:')
a=[]

for i in range (0,n,1):
    a.append(input('Digite um elemento:'))

print (a[0])

print(a[n-1])

media=0

for i in range (0,n,1):
    media=media+a[i]

m=media/(len(a))
print ('%f.2'%m)

print (a)