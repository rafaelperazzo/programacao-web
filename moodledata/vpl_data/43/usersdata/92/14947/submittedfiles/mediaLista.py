# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite um valor: ')
a= []

for i in range (1, n+1, 1):
    a.append(input('Digite um valor: '))
    
media=0
for i in range(0, n, 1):
    media= media+ a[i]
media= media/n

u= n-1

print(a[0])
print(a[u])
print(media)
print(a)
