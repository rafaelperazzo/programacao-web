# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite o valor de a: '))
b=int(input('digite o valor de b: '))

mdc=1
if a>b:
    maior= a
else:
    maior= b
for i in range (1, maior):
    if a%i==0 and b%i==0:
        mdc=i
print mdc 