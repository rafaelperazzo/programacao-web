# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o valor decimal a ser convertido: ')

i = 1
j = 1
while n>=i:
    k = i%2
    i = i*2
    print('%d'% k)