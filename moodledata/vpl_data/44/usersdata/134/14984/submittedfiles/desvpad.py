# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n = input('Digite o valor de n:')
a = []
soma = 0
for i in range (0,n,1):
    a.append(input('Digite o elemento:'))
    soma = soma + a[i]
    media = soma/n
somatorio = 0
for i in range (0,n,1):
    somatorio = somatorio + (a[i]-media)
    s = (1/(n-1))*somatorio
print ('%.2f' %a[0])
print ('%.2f' %a[n-1])
print ('%.2f' %media)
print ('%.2f' %s)
