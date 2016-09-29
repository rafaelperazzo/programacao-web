# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o número de a:'))
b = int(input('Digite o número de b:'))
c = int(input('Digite o número de c:'))
d = int(input('Digite o número de d:'))
e = int(input('Digite o número de e:'))

if a < b and a < c and a < d and a < e:
    print('a')
elif b < a and b < c and b < d and b < e:
    print('b')
elif c < a and c < b and c < d and c < e:
    print('c')
elif d < a and d < b and d < c and d < e:
    print('d')
else:
    print('e')
if a > b and a > c and a > d and a > e:
    print('a')
elif b > a and b > c and b > d and b > e:
    print('b')
elif c > a and c > b and c > d and c > e:
    print('c')
elif d > a and d > b and d > c and d > e:
    print('d')
else:
    ('e')