# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite n:')
l=[]
i=0
soma=0
while i<n:
    l.append(input('Digite um valor para a lista:'))
    i=i+1

while i<n:
    soma=soma+l[i]
    i=i+1
    
media=soma/n

print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %media)
print l  