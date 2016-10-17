# -*- coding: utf-8 -*-
from __future__ import division
import math

cont = 1
a = int(input('Digite o algarismo a: '))
b = int(input('Digite o algarismo b: '))
if a >= b:
    i = a
    j = b
    while i%j >= 0:
        cont = cont + 1
        i = j
        j = i%j
elif b > a:
    i = b
    j = a
    while i%j > 0:
        cont = cont + 1
        i = j
        j = i%j
print('%d' %j)
print('%d' %cont)