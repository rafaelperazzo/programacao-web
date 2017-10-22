# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

x = float(input('Digite o investimento inicial: '))
y = float(input('Digite a taxa de crescimento anual: '))
y = y/100

c = 1
while (c<11):
    print(x + (x*y*c))
    c = c + 1