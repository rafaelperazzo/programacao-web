# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite a quantidade de termos: ')

i = 1
b = 0
d = 0
while n >= i:
    if i%2 != 0:
        a = 1/1
        b = b + a
    elif i%2 == 0:
        c = -1/i
        d = d + c
S = b + d
i = i + 1
print('%.5' %S)