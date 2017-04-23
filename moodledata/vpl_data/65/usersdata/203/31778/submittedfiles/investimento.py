# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento=float(input('Investimento inicial: '))
taxa=float(input('Taxa de crescimento decimal: '))
for i in range (1,11,1):
    investimento=investimento+investimento*taxa
    print('cu %.2f' % investimento)