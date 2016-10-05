# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite n: '))

i = 2
j = 2
s = 1

if n == 1:
    print('%d'% (s))

while i>=n:
    x = -(i)/(j*j) + (i+1)/(j+1)**2
    s = s + x
    i = i+1
    j = j+2