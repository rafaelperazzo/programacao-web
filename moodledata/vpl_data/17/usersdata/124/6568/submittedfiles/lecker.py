# -*- coding: utf-8 -*-
from __future__ import division
import math
a = input('Digite o valor da variável a: ')
b = input('Digite o valor da variável b: ')
c = input('Digite o valor da variável c: ')
d = input('Digite o valor da variável d: ')

if (a > b):
    print('S')
if (b > a) and (b > c):
    print('S')
if (c > b) and (c > d):
    print('S')
if (d > c):
    print('S')
else:
    print('N')