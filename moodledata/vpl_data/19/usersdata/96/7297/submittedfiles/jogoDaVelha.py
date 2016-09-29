# -*- coding: utf-8 -*-
from __future__ import division
import math

x1 = input('Digite o valor de x1:')
x2 = input('Digite o valor de x2:')
x3 = input('Digite o valor de x3:')
x4 = input('Digite o valor de x4:')
x5 = input('Digite o valor de x5:')
x6 = input('Digite o valor de x6:')
x7 = input('Digite o valor de x7:')
x8 = input('Digite o valor de x8:')
x9 = input('Digite o valor de x9:')

if x1 == x2 == x3 or x4 == x5 == x6 or x7 == x8 == x9 or x1 == x4 == x7 or x2 == x5 == x8 or x3 == x6 == x9 or x1 == x5 == x9 or x3 == x5 == x7:
    print('0')
elif x1 == x2 == x3 or x4 == x5 == x6 or x7 == x8 == x9 or x1 == x4 == x7 or x2 == x5 == x8 or x3 == x6 == x9 or x1 == x5 == x9 or x3 == x5 == x7:
    print('1')
else:
    print('E')
    

