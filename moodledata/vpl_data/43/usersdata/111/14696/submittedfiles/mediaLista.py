# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n: ')

a=[]
b=0
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
    b=b+a[i]
    
media=(b/n)

print %.2f (%a[0])
print %.2f (%a[n-1])

print %.2f (%media)
