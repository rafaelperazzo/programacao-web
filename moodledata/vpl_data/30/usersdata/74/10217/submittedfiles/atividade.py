# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite o valor de n: '))

i = 1
s = 1/n

while n>=i:
    x = (i+1)/(n-i)
    s = s+x
    i = i+1
print('%d'%(s))