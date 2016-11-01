# -*- coding: utf-8 -*-
from __future__ import division

n = input('digite a quantidade de numeros: ')
L = [n]
soma = 0
x = 0
while x<=n-1:
    soma += L[x]
    x += 1
    
print ('%2.f' % (soma/x))
