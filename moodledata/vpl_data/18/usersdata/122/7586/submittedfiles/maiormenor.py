# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número a: ')
b = input('Digite o número b: ')
c = input('Digite o número c: ')
d = input('Digite o número d: ')
e = input('Digite o número e: ')

#CONTINUE...
if a>b and a>c and a>d and a>e:
    print(a)
elif b>a and b>c and b>d and b>e:
    print(b)
elif c>a and c>b and c>d and c>e:
    print(c)
elif d>a and d>b and d>c and d>e:
    print(d)
elif e>a and e>b and e>c and e>d:
    print(e)
elif a<b and a<c and a<d and a<e:
    print (a)
elif b<a and b<c and b<d and b<e:
    print(b)
elif c<a and c<b and c<d and c<e:
    print(c)
elif d<b and d<c and d<c and d<e:
    print(d)
elif e<b and e<c and e<d and e<d:
    print(e)