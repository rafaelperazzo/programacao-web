# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite n:')
l=[]
i=0
soma=0
while i<n:
     l.append(input('Digite um valor para a lista:'))
     i=i+1
i=0
while i<n:
     soma=soma+l[i]
     i=i+1
     
media=soma/n

i=0
soma=0
while i<n:
    soma=soma+(l[i]-media)
    i=i+1
s= ((1/(n-1))*(soma**2))**0.5

print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %media)
print ('%.2f' %s)