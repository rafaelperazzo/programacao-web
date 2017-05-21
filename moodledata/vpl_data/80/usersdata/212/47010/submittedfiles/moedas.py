# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('digite o valor da primeira moeda:'))
a=int(a)
b=float(input('digite o valor da segunda moeda:'))
b=int(b)
c=float(input('digite o valor da cédula:'))
c=int(c)
if a>=b:
    ma=a
    me=b
else:
    ma=b
    me=a
if (c%ma)==0:
    qma=(c/ma)
    qme=0
else:
    while c<= 