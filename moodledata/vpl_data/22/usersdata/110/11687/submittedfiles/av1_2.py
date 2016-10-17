# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
d=int(input('Digite d: '))
if a==c or b==d:
    print('V')
if a==d and b!=c:
    print('F')


