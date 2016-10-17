# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
d=int(input('digite o valor de d:'))
if a==c or d==b and a!=b:
    print('V')
if a==d and b==c:
    print('F')
else:
    print('F')