# -*- coding: utf-8 -*-
from __future__ import division

P = input('Digite o valor de P: ')
i = input('Digite o valor de i: ')
n = input('Digite o valor de n: ')

v = P * ((((1 + i)**n) -1) / i)

print('O valor de v é: %.2f' % (v))