# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...
if a<=b and a<=c and a<=d and a<=e:
    print (a)
elif b<=a and b<=c and b<=d and b<=e:
    print (b)
elif c<=a and c<=b and c<=d and c<=e:
    print (c)
elif d<=b and d<=c and d<=a and d<=e:
    print (d)
else:
    print (e)
if a>=b and a>=c and a>=d and a>=e:
    print (a)
elif b>=a and b>=c and b>=d and b>=e:
    print (b)
elif c>=a and c>=b and c>=d and c>=e:
    print (c)
elif d>=a and d>=b and d>=c and d>=e:
    print (d)
else:
    print (e)