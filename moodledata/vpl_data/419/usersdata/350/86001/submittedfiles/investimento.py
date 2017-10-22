# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

n = float(input('Digite o valor do investimento: '))
t = float(input('Digite o valor da taxa: '))
cont = 0
while cont<10:
    n = (n + (n*t))
    print('%.2f' % n)
    cont += 1 