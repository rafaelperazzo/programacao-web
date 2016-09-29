# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a<=b and a<=c and a<=d and a<=e:
    print('%d'% (a))
    if b>=c and b>=d and b>=e:
        print('%d'% (b))
    elif c>=b and c>=d and c>=e:
        print('%d'% (c))
    elif d>=b and d>=c and d>=e:
        print('%d'% (d))
    else:
        print('%d'% (e))
elif b<=a and b<=c and b<=d and b<=e:
    
