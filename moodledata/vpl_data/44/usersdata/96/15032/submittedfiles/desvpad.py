# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n = input('Digite o valor de n:')
a = []

soma = 0
for i in range(0,n,1):
    soma = soma + a[i]

media = soma/len(a)

somatorio = 0 
for i in range(0,n,1):
    somatorio = somatorio + (a[i] - media)**2

dp = (somatorio/(n - 1)**0.5

print('%.2f' %a[0])
print('%.2f' %a[n-1])
print('%.2f' %media)
print('%.2f' %dp)

