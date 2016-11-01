# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('digite a quantidade de n:'))
l=[]


for i in range(0,n,1):
    l.append(input('digite a quantidade de n:'))
    
soma = 0
for i in range (0,n,1):
    soma=soma+l[i]
    
media=soma/n
    
print ('%.2f'%l[0])
print ('%.2f'%l[n-1])
print ('%.2f'%media)
print (l)

