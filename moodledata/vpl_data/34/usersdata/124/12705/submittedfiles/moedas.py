# -*- coding: utf-8 -*-
from __future__ import division

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if a > b:
    if (c//a)//b > 0:
        print(c//a)
        print((c//a)//b)
    else:
        print('N')