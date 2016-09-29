# -*- coding: utf-8 -*-
from __future__ import division

a = input('')
b = input('')
c = input('')
d = input('')

if (a == b+c+d) and (d == b+c) and (b == c):
    print('S')
else:
    print('N')
    