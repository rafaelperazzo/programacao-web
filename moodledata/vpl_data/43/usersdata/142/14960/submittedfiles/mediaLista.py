# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite um número n:')
L = []

for i in range (0,n,1):
    L.append(input('Digite um valor:))

soma=0
for i in range (0,n,1):
    soma = soma + L[i]

media = soma/n

print ('%.2f'%L[0])
print ('%.2f'%L[n])
print ('%.2f'%media)
print L