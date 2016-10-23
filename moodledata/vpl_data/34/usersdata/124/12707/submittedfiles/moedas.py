# -*- coding: utf-8 -*-
from __future__ import division

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if a > b:
    d = c//a
    if d//b > 0:
        print(c//a)
        print((c%a)//b)
    else:
        print('N')
elif b > a:
    d = c//b
    if d//a > 0:
        print(c//b)
        print((c%b)//a)
    else:
        print('N')