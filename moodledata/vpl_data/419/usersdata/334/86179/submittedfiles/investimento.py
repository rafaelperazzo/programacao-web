# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

x = float(input('Digite o investimento inicial: '))
y = float(input('Digite a taxa de crescimento anual: '))
y = y/100

v = x + (x*y)

c = 1
while (c<11):
    print(v)
    c = c + 1