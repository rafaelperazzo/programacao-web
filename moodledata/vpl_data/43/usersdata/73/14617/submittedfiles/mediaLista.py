# -*- coding: utf-8 -*-
from __future__ import division
n=input('quantidade de valores:')
l=[]
for i in range (0,n,1):
    l.append(input('digite o elemento:'))
soma=0
for j in range (0,n,1):
    soma=soma+l[j]
    print soma
media=soma/n

print ('%.2f'%l[0])
print ('%.2f'%l[n])    
print ('%.2f'%media)
print ('%.2f'%l)