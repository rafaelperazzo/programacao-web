# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite a quantidade de termos: ')

b = 0
d = 0
for i in range (1, n+1, 1):
    if i%2 != 0:
        a = 1/i
        b = b + a
    elif i%2 == 0:
        c = -1/i
        d = d + c
i = i + 1
S = b + d
print(S)