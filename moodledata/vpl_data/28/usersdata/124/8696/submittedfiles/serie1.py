# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite a quantidade de termos: ')

i = 1
S = 0
while n >= i:
    if i%2 != 0:
        a = 1/1
        S = S + a
    elif i%2 == 0:
        a -1/i
        S = S + a
print('%.5' %S)
i = i + 1