# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA

p = input('Digite o valor de P: ')
i = input('Digite o valor de I: ')
n = input('Digite o valor de N: ')

#PROCESSAMENTO

v = float(p* ((((1 + i)**n) - 1) / i))

#SAÍDA

print('O valor de v é: %.2f' % v)