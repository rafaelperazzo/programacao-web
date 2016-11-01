# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de elementos da lista:')
a=[]

for i in range (0,n,1):
    a.append(input('Digite um elemento:'))

print (a[0])

s=(len(n))
j=a[s]
print(j)

media=0

for i in range (1,n+1,1):
    media=media+a[i]

m=media/(len[n])
print (m)

print (a[n])