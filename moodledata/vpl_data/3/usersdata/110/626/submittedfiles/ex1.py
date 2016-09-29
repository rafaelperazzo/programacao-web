# -*- coding: utf-8 -*-
from __future__ import division
a=input('Digite a: ')
b=input(' Digite b: ')
c=input( ' Digite c: ')
if a<b and b<c:
    print(c)
if a<c and c<b :
    print(b)
if c<b and b<a:
    print(a)
if c=b=a:
    print(a)