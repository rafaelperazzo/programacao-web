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

j=0
soma2=0
while j<n:
    soma2=soma2+(l[j]-media)**2
    j=j+1
s= (((1/(n-1))*soma2)**0.5

print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %media)
print ('%.2f' %s)