# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o avlor de n:')
a = []
soma=0

for i in range (0,n,1):
    a.append(input('Digite o elemento:'))
    soma = soma + a[i]
media = soma/n
    
print a[0]
print a[n-1]


