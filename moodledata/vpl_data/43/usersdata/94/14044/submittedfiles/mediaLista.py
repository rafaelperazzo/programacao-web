# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de valores da lista:')
l=[]

for i in range(0,n,1):
    l.append(input('digite o elemento:'))
   
print('%.2f' %l[0])
print('%.2f' %sum(l)/n)

