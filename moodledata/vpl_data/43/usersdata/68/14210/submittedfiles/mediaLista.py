# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite n:')
l=[]
i=0
soma=0
while i<n:
    l.append(input('Digite um valor para a lista:'))
    i=i+1

foi i in range (0,n,1):
    soma=soma+ l[i]

media=soma/n

print ('%.2f' %l[0])
print ('%.2f' %l[n-1])
print ('%.2f' %media)
print l  