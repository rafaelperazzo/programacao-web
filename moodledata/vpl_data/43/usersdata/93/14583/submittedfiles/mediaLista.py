# -*- coding: utf-8 -*-
from __future__ import division
n
a=[]
for i in range(0,n,1):
    a.append(input('proximo elemento da lista: '))
maior=a[0]
menor=a[0]
for i in range (0,n,1):
    if a[i]>maior:
        maior=a[i]
    if a[i]<menor:
        menor=a[i]
print(maior)
print(menor)
print(a)