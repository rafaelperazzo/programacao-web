# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o avlor de n:')
a = []
soma=0

for i in range (0,n,1):
    a.append(input('Digite o elemento:'))
    soma = soma + a[i]
media = soma/n
    
print ('%.2f' %a[0])
print ('%.2f' %a[n-1])
print ('%.2f' %media)
print a

