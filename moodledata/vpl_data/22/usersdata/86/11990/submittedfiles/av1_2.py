# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('digite a:'))
b = int(input('digite b:'))
c = int(input('digite c:'))
d = int(input('digite c:'))

if a==c and a!=b and c!=d and c!=b:
    if b!=d:
        print('V')
    else:
        print('F')
elif b==d and a!=b and c!=d and c!=b:
    if a!=c:
        print('V')
    else:
        print('F')
else:
    print('F')