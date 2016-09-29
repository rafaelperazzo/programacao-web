# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...

if a>b and c<=b and d<=b and e<=b:
    print (a)
elif b>a and c<=a and d<=a and e<=a:
    print (b)
elif c>b and a<=b and d<=b and e<=b:
    print (c)
elif d>c and a<=b and b<=c and e<=b:
    print (d)
elif e>d and c<=d and b<=d and a<=d:
    print (e)
    
if a<b and b>=b and d>=b and e>=b:
    print (a)
elif b<a and c>=a and d>=a and d>=a:
    print (b)
elif c<b and a>=b and d>=b and e>=b:
    print (c)
elif d<c and a>=b and b>=c and e>=b:
    print (d)
elif e<d and c>=d and b>=d and a>=d:
    print (e)
    
    