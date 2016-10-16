# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('a:')
b=input('b:')
c=input('c:')
d=input('d:')
if a>b and a>c and a>d:
    maior=a
    if b>a and b>c and b>d:
        maior=a
    if c>a and c>b and c>d:
        maior=c
    if d>a and d>b and d>c:
        maior=d

elif a<b and a<c and a<d:
    menor=a
    if b<a and b<c and b<d:
        menor=b
    if c<a and c<b and c<d:
        menor=c
    if d<a and d<b and d<c:
        menor=d
print (menor,maior)
