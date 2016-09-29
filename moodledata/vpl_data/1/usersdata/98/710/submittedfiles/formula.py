# -*- coding: utf-8 -*-
from __future__ import division

p=input('Informe o valor de p: ')
i=input('Informe o valor de i: ')
n=input('Informe o valor de n: ')

v=(p*(((1+i)**n)-1)/i)

print('%.2f' %v)