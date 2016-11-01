# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores da lista:')
l= []

for i in range (0,n,1):
    l.append(input('Digite o elemento da lista:'))
    
ma=sum(l)/n
print ('%.2f' %l[0])
print ('%.2f' %u)
print ('%.2f' %ma)
print (l)