# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('digite um valor para a:')
b = input('digite um valor para b:')
c = input('digite um valor para c:')
d = input('digite um valor para d:')

if a<b>c and c>d:
    print('S')
elif b<a and c>d and b>c:
    print('S')
elif b<c>d and b>a:
    print('S')
elif d>c and c>b and b>a:
    print('S')
else:
    print('N')