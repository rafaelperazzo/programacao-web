# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
d=input('digite o valor de d:')

if a<b<c<d:
    print('s')
if a==b==c==d:
    print('n')
if a<b>c<d:
    print('n')
if a<b>c>d:
    print('s')
    

