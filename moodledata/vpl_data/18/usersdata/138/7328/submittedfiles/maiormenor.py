# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o número a:')
b=input('Digite o número b:')
c=input('Digite o número c:')
d=input('Digite o número d:')
e=input('Digite o número e:')
if a<b and a<c and a<d and a<e:
    print(a)
    if b>a and b>c and b>d and b>e:
        print(b)
    elif c>b and c>d and c>e and c>a:
        print(c)
    elif d>b and d>c and d>e and d>a:
        print(d)
    elif e>a and e>b and e>c and e>d:
        print(e)
elif b<a and b<c and b<d and b<e:
    print(b)
    if b<a and a>c and a>d and a>e:
        print(a)
    elif c>b and c>d and c>e and c>a:
        print(c)
    elif d>b and d>c and d>e and d>a:
        print(d)
    elif e>a and e>b and e>c and e>d:
        print(e)
elif c<b and a<c and c<d and c<e:
    print(c)
    if b>a and b>c and b>d and b>e:
        print(b)
    elif a>b and a>d and a>e and a>a:
        print(a)
    elif d>b and d>c and d>e and d>a:
        print(d)
    elif e>a and e>b and e>c and e>d:
        print(e)
elif d<b and d<c and a>d and d<e:
    print(d)
    if b>a and b>c and b>d and b>e:
        print(b)
    elif c>b and c>d and c>e and c>a:
        print(c)
    elif a>b and a>c and a>e and a>d:
        print(a)
    elif e>a and e>b and e>c and e>d:
        print(e)
elif e<b and e<c and e<d and a>e:
    print(e)
    if b>a and b>c and b>d and b>e:
        print(b)
    elif c>b and c>d and c>e and c>a:
        print(c)
    elif d>b and d>c and d>e and d>a:
        print(d)
    elif e<a and a>b and a>c and a>d:
        print(a)



