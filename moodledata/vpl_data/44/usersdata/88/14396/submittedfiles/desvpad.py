# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n=input('Digite a quantidade de elementos: ')
l=[]

for i in range (0,n,1):
    l.append(input('Digite o valor do elemento: '))
   
soma=0
for i in range (0,n,1):
    soma=(soma+l[i])
media=soma/n

for i in range (0,n,1):
    soma=(l[i]-media)**2
s=(((1/(n-1))*soma))**0.5

print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %media)
print ('%.2f' %s)