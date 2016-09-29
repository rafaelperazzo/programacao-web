# -*- coding: utf-8 -*-
from __future__ import division

a = input('Digite o primeiro valor')
b = input('Digite o segundo valor')
c = input('Digite o terceiro valor')

if a>=b and a>=c:
    print('%.2f'% a)
elif b>=a and b>=c:
    print('%.2f'% b)
else:
    print('%.2f'% c)