# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite o valor de n: '))

i = 0
s = 0

while n>i:
    x = (i+1)/(n-i)
    s = s+x
    i = i+1
print('%.5f'%(s))