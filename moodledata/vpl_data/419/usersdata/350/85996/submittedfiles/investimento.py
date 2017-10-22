# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

n = float(int('Digite o valor do investimento: '))
t = float(int('Digite o valor da taxa: '))
cont = 0
while cont<0:
    n = (n + (n*t))
    print('%2.f' % n)
    cont += 1 