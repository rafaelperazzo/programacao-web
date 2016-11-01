# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n = input('Digite o valor de n: ')
x = []

for i in range (0,n,1):
    x.append(input('Digite um elemento: '))
media = sum(x)/n

soma = 0

for j in range (0,n,1):
    soma = soma+(x[j]-media)**2
s = ((x/(n-1))*soma)**0.5

print('%.2f' % x[0])
print('%.2f' % x[n-1])
print('%.2f' % media)
print('%.2f' % s)