# -*- coding: utf-8 -*-
from __future__ import division
import math

cont = 1
a = int(input('Digite o algarismo a: '))
b = int(input('Digite o algarismo b: '))
if a >= b:
    i = a
    j = b
    while True:
        i%j = c
        if c > 0:
            cont = cont + 1
            i = j
            j = c
        elif i%j == 0:
            break
elif b > a:
    i = b
    j = a
    while True:
        i%j = d
        if d > 0:
            cont = cont + 1
            i = j
            j = d
        elif i%j == 0:
            break
print('%d' %j)
print('%d' %cont)