# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')
if a<=b<=c<=d<=e:
    print(a)
elif b<=a<=c<=d<=e :
    print(b)
if c<=a<=b<=d<=e:
    print(c)
elif d<=a<=b<=c<=e:
    print(d)
if e<=a<=b<=c<=d<=e:
    print(e)
if a>=b>=c>=d>=e:
    print(a)
elif b>=a>=c>=d>=e:
    print(b)
if c>=b>=a>=d>=e:
    print(c)
elif d>=a>=b>=c>=e:
    print(d)
if e>=a>=b>=c>=d>=e:
    print(e)
    
    
