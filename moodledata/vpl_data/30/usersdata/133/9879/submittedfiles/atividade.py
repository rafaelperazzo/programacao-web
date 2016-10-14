# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite n:'))
while n<0:
    print(" n é um inteiro positivo')
    n=int(input('Digite n:'))

s=0
for i in range (0, n, 1):
    s = s +((i+1)/(n-i))
print ('%.5f' %s)
