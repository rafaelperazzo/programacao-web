# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
if a > b and a > c and a > d and a > e:
    print('%d'%a)
    if b < c and b < d and b < e:
        print('%d' %b)
    elif c < b and c < d and c < e:
        print('%d' %c)
    elif d < c and d < b and d < e:
        print('%d' %d)
    if e < c and e < d and e < b:
        print('%d' %e)
elif b > a and b > c and b > d and b > e:
    print('%d' %b)
    if a < c and a < d and a < e:
        print('%d' %a)
    elif c < a and c < d and c < e:
        print('%d' %c)
    elif d < c and d < a and d < e:
        print('%d' %d)
    elif e < c and e < d and e < a:
        print('%d' %e)
elif c > a and c > b and c > d and c > e:
    print('%d' %c)
    if a < b and a < d and a < e:
        print('%d' %a)
    elif b < a and b < d and b < e:
        print('%d' %b)
    elif d < a and d < b and d < e:
        print('%d' %d)
    elif e < b and e < d and e < a:
        print('%d' %e)
elif d > a and d > b and d > c and d > e:
    print('%d' %d)
    if a < b and a < c and a < e:
        print('%d' %a)
    elif b < a and b < c and b < e:
        print('%d' %b)
    elif c < b and c < a and c < e:
        print('%d' %c)
    elif e < b and e < c and e < a:
        print('%d' %e')
elif e > a and e > b and e > c and e > d:
    print('%d' %e)
    if a < b and a < c and a < d:
        print('%d' %a)
    elif b < a and b < c and b < d:
        print('%d' %b)
    elif c < b and c < a and c < d:
        print('%d' %c)
    elif d < b and d < c and d < a:
        print('%d' %d)