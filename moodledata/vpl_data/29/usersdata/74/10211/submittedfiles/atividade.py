# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite o numero: '))

i = 1
j = 10

while n>=j:
    if n/j>=1:
        i = i+1
    j = j*10
print('%d'%(i))