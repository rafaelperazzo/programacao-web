# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))
e = int(input('Digite o quinto número: '))

if a<b and a<c and a<d and a<e:
    print(a)
if b<a and b<c and b<d and b<e:
    print(b)
if c<a and c<b and c<d and c<e:
    print(c)
if d<a and d<b and d<c and d<e:
    print(d)
if e<a and e<b and e<d and e<c:
    print(e)

if a>b and a>c and a>d and a>e:
    print(a)
if b>a and b>c and b>d and b>e:
    print(b)
if c>a and c>b and c>d and c>e:
    print(c)
if d>a and d>b and d>c and d>e:
    print(d)
if e>a and e>b and e>d and e>c:
    print(e)