# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

x = float(input('Digite o investimento inicial: '))
y = float(input('Digite a taxa de crescimento anual: '))

x = x + (x*y)
c = 0

while (c<10):
    print(x)
    c = c + 1