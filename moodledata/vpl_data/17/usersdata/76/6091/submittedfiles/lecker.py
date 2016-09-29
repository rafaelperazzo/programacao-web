# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite a:')
b = input('Digite b:')
c = input('Digite c:')
d = input('Digite d:')

if a>b and b>c and c>d:
    print('S')
elif a<b and b<=c and c>d:
    print('S')
elif a<b and b>c and c>d:
    print('S')
elif a<b and b<c and c<d:
    print('S')
else:
    print('N')