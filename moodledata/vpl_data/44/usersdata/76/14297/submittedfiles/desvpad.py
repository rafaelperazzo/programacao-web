# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n = input('Digite o valor de n: ')
x = []

for i in range (0,n,1):
    x.append(input('Digite um elemento: '))
media = x[0]
for i in range (1,n,1):
    media = media + x[i]
media = media/n

print('%.2f' % x[0])
print('%.2f' % x[n-1])
print('%.2f' % media)