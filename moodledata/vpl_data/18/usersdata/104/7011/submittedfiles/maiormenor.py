# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...
if a>b and a>c and a>d and a>e:
    print(a)
    if b<c and b<d and b<e:
        print(b)
    elif c<d and c<e:
        print(c)
    elif d<e:
        print(d)
    else:
        print(e)
elif b>c and b>d and b>e:
    print(b)
    print(a)
elif c>d and c>e:
    print(c)
    if a>b:
        print(b)
    else:
        print(a)
elif d>e:
    print(d)
    if a<b and a<c:
        print(a)
    elif b<c:
        print(b)
    else:
        print(c)
else:
    print(e)
        if a<b and a<c and a<d:
            print(a)
        elif b<c and b<d:
            print(b)
        elif c<d:
            print(c)
        else:
            print(d)
