# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a>=b and a>=c and a<=d:
    print('%.f' %a)
elif b>=a and b>=c and b>=d:
    print('%.f' %b)
elif c>=a and c>=b and c>=d:
    print('%.f' %c)
elif d>=a and d>=b and d>=c:
    print('%.f' %d)
    
if a<=b and a<=c and a<=d:
    print('%.f' %a)
elif b<=a and b<=c and b<=d:
    print('%.f' %b)
elif c<=a and c<=b and c<=d:
    print('%.f' %c)
elif d<=a and d<=b and d<=c:
    print('%.f' %d)