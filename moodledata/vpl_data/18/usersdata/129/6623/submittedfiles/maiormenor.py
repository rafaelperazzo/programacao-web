# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...
if a>=b>=c>=d>=e:
    print a
elif b>=a>=c>=d>=e:
    print b
elif c>=b>=a>=d>=e:
    print c
elif d>=b>=c>=a>=e:
    print d
elif e>=b>=c>=d>=a:
    print e
if a<=b<=c<=d<=e:
    print a
elif b<=a<=c<=d<=e:
    print b
elif c<=b<=a<=d<=e:
    print c
elif d<=b<=c<=a<=e:
    print d
elif e<=b<=c<=d<=a:
    print e
    