# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de valores da lista:')
l=[]

for i in range (0,n,1):
    l.append(input('Digite o elemento da lista:'))
    
ma=sum(l)/n
soma=0

for j in range(0,n,1):
    soma=soma+(((l[j])-ma)**2)
    
s=((1/(n-1))*soma)**(1/2)

print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %ma)
print ('%.2f' %s)