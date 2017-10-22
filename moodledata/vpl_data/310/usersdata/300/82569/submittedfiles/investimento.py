# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i = float(input('Digite o valor do investimento inicial: '))
t = float(input('Digite o valor da taxa de crescimento percentual: '))
a = 0
while a<10:
    i = i + t*i
    print('%.2f' % i)
    a = a + 1
    
