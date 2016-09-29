# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')
if a<b and a<c and a<d and a<e:
    print('a')
    if b>=c and b>=d and b>=e:
        print('b')
    elif c>=b and c>=d and c>=e:
        print('c')
    elif d>=b and d>=c and d>=e:
        print('d')
    else:
        print('e')
elif b<a and b<c and b<d and d<e:
    print('b')
    if a>=c and a>=d and a>=e:
        print('a')
    elif c>=a and c>=d and c>=e:
        print('c')
    elif d>=a and d>=c and d>=e:
        print('d')
    else:
        print('e')
elif c<a and c<b and c<d and c<e:
    print('c')
    if a>=b and a>=d and a>=e:
        print('a')
    elif b>=a and b>=d and b>=e:
        print('b')
    elif d>=a and d>=b and d>=e:
        print('d')
    else:
        print('e')
elif d<a and d<b and d<c and d<e:
    print('d')
     if a>=b and a>=c and a>=e:
        print('a')
    elif b>=a and b>=c and b>=e:
        print('b')
    elif c>=a and c>=b and c>=e:
        print('c')
    else:
        print('e')
else:
    if a>=b and a>=c and a>=d:
        print('a')
    elif b>=a and b>=c and b>=d:
        print('b')
    elif c>=a and c>=b and c>=d:
        print('c')
    else:
        print('d')
    