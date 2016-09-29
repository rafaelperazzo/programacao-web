# -*- coding: utf-8 -*-
from __future__ import division
n = input('Digite a quantidade de lados:')
if n>2:
    nd = n*(n-3)/2
print('Quantidade de diagonais:%.1f'%nd)