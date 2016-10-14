# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite o valor de n: '))
if n > 0:
    a = 1
    b = n
    S = 0
    while a < n:
        c = a/b
        a = a+1
        b = b-1
        S = S + c
print('%.5f' %S)
elif n < 0:
    a = 1
    b = -n
    S = 0
    while a < -n:
        c = a/b
        a = a+1
        b = b-1
        S = S + c
print('%.5f' %S)