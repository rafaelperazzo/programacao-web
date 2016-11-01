# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de termos:')
L = [ ]
for i in range(0,n,1):
    L.append(input('Digite o valor:'))
    
soma = 0
for j in range(0,n,1):
    soma = soma + L[j]

M = soma/n

print(L[0])
print(L[n-1])
print(M)
print(L)