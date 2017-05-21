# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de A:'))
b=int(input('digite o valor de B:'))
c=int(input('digite o valor de C:'))
if a>b:
    while c>0:
        x=c//a
        r=c%a
        s=r//b
        print(x)
        print(s)
        break
if a<b:
    while c>0:
        y=c//b
        print(b)
        break