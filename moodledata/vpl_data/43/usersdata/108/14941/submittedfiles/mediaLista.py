# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite n:')
l = []
soma=0
media=0

for i in range (0,n,1):
    l.append(input('Digite o valor:'))
    
print ('%.2f' %l[0])
print ('%.2f' %l[n-1])

for i in range (0,n,1):
    soma = soma + l[i]

media = soma/n

print ('%.2f' %media)
print (lista)

    
    