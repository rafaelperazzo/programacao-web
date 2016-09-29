# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
i = input('Digite o valor do investimento: ')
t = input('Digite a taxa de crescimento: ')
I1 = 1000 + i*t
I2 = I1 + I1*t
I3 = I2 + I2*t
I4 = I3 + I3*t
I5 = I4 + I4*t
I6 = I5 + I5*t
I7 = I6 + I6*t
I8 = I7 + I7*t
I9 = I8 + I8*t
I10 = I9 + I9*t
print('%.2f' %I1)
print('%.2f' %I2)
print('%.2f' %I3)
print('%.2f' %I4)
print('%.2f' %I5)
print('%.2f' %I6)
print('%.2f' %I7)
print('%.2f' %I8)
print('%.2f' %I9)
print('%.2f' %I10)