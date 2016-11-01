# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite a quantidade de valores:')
l=[]


for i in range (0,n,1):
    l.append(input('Digite um elemento:'))

soma=0    
for i in range (0,n,1):
    soma=soma+l[i]
    
media=soma/n
z=0
somatorio=0
for i in range (1,n+1,1):
    somatorio=((l[z]-media)**2)+somatorio
    z=z+1
somatorio=somatorio*(1/(n-1))
somatorio=somatorio**(1/2)

print ('%.2f'%l[0])
print ('%.2f'%l[n-1])
print ('%.2f'%media)
print (l)
print ('%.2f' %somatorio)