# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

if a>(b and c and d and e):
    print(a)
if b>(c and d and a and e):
    print(b)
if c>(a and b and d and e):
    print(c)
if d>(a and b and c and e):
    print(d)
if e>(a and b and c and d):
    print(e)
if a<(b and c and d and e):
    print(a)
if b<(c and d and a and e):
    print(b)
if c<(a and b and d and e):
    print(c)
if d<(a and b and c and e):
    print(d)
if e<(a and b and c and d):
    print(e)
