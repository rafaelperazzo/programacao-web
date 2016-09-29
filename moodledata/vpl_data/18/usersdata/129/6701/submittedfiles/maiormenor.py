# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número : ')
b = input('Digite o número : ')
c = input('Digite o número : ')
d = input('Digite o número : ')
e = input('Digite o número : ')

#CONTINUE...
if a<b and a<c and a<d and a<e:
    print a
else b<a and b<c and b<d and b<e:
    print b
else c<a and c<b and c<d and c<e:
    print c
else d<b and d<c and d<a and d<e:
    print d
else e<b and e>c and e<d and e<a:
    print e
if a>b and a>c and a>d and a>e:
    print a
else b>a and b>c and b>d and b>e:
    print b
else c>a and c>b and c>d and c>e:
    print c
else d>b and d>c and d>a and d>e:
    print d
else e>b and e>c and e>d and e>a:
    print e