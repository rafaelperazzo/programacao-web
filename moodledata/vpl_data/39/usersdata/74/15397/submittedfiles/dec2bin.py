# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o valor decimal a ser convertido: ')

while n>=0.9:
    k = n%2
    n = n%2
    print('%d'% k)