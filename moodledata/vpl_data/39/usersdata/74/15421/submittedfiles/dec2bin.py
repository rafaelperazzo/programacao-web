# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o valor decimal a ser convertido: ')

i = 0
b = 0

while n>=0.9:
    k = n%2
    b = b+(k*10**i)
    n = n/2
    i = i+1
print('%d'% b)