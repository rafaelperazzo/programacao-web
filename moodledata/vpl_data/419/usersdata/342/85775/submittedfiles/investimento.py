# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

n = float(input('Valor de investimento inicial:'))
t = float(input('Taxa de crescimento percentual:'))

e = 1
while e<11:
    valorfinal = n*((1+t)**e)
    print (" %2.f" %valorfinal)
    e=e+1