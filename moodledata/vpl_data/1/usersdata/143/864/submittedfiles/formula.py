# -*- coding: utf-8 -*-
from __future__ import division
p = input ('Valor de P')
i = input('Valor de i')
n = input('Valor de n')

v = p*(((1+i)**n)-1)/(i)

print('%.2f'%v)