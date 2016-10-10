# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite a quantidade de múltiplos: ')
a = input('Digite o número a: ')
b = input('Digite o número b: ')

i = 0
c = 1
while True:
    if c%a == 0 or c%b == 0 or c%a == 0 and c%b == 0:
        print(c)
        i = i + 1
        if i == n:
            break
    else:
        c = c + 1