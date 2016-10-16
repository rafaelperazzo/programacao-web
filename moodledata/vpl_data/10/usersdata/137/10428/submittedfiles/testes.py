# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('a:')
b=input('b:')
c=input('c:')
d=input('d:')
maior=a
menor=a
if menor>b:
    menor=b
if menor>c:
    menor=b
if menor>d:
    menor=d
if maior<b:
    maior=b
if maior<c:
    maior=c
if maior<d:
    maior=d
print menor
print maior