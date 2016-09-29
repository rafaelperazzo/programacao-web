# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a>b and a>c and a>d and a>e or a==b or a==c or a==d or a==e:
    print(a)
if b>c and b>d and b>a and b>e or b==a or b==c or b==d or b==e:
    print(b)
if c>a and c>b and c>d and c>e or c==b or c==a or c==d or c==e:
    print(c)
if d>a and d>b and d>c and d>e or d==b or d==c or d==a or d==e:
    print(d)
if e>a and e>b and e>c and e>d or e==b or e==c or e==d or a==e:
    print(e)
if a<b and a<c and a<d and a<e or a==b or a==c or a==d or a==e:
    print(a)
if b<c and b<d and b<a and b<e or a==b or b==c or b==d or b==e:
    print(b)
if c<a and c<b and c<d and c<e or c==b or a==c or c==d or c==e:
    print(c)
if d<a and d<b and d<c and d<e or d==b or d==c or a==d or d==e:
    print(d)
if e<a and e<b and e<c and e<d or e==b or e==c or e==d or a==e:
    print(e)
