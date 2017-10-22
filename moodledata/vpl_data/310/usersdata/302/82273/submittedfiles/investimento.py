# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = float(input('Digite o valor do investimento inicial: '))
t = float(input('Digite a taxa de crescimento percentual: '))
i = 0
t = t+1
while i<10:
    v = v*t
    i = i+1
    print('%.f2'%v)
