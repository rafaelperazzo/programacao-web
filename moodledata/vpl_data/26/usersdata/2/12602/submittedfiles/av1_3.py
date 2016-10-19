# -*- coding: utf-8 -*-
from __future__ import division
import math

a =input('Digite a: ')
b = input('Digite b: ')

contA = 0

while a>=1:
    a = a//10
    contA = contA + 1

contB = 1
b = b*10

frac = b - int(b)
while frac>0:
    b = b*10
    frac = b - int(b)
    print frac
    contB = contB + 1
print contA
print contB
