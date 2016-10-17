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
        if i%j > 0:
            cont = cont + 1
            i = j
            j = i%j
        elif i%j == 0:
            break
elif b > a:
    i = b
    j = a
    while True:
        if i%j > 0:
            cont = cont + 1
            i = j
            j = i%j
        elif i%j == 0:
            break
print('%d' %j)
print('%d' %cont)