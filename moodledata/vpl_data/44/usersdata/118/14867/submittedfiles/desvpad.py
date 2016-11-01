# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo


n = input('Digite a quantidade de termos:')
L = [ ]
for i in range(0,n,1):
    L.append(input('Digite o valor:'))
    
soma = 0
for j in range(0,n,1):
    soma = soma + L[j]
M = soma/n

somatorio = 0
for a in range(0,n,1):
    somatorio = somatorio + ((L[a] - M)**2)
s = (((1/(n-1))*somatorio)**0.5)
   
print('%.2f' %L[0])
print('%.2f' %L[(n-1)])
print('%.2f' %M)
print('%.2f' %s)