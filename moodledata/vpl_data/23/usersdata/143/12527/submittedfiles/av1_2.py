# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite valor de n: ')
x1=input('digite valor de x1: ')
y1=input('digite valor de y1: ')
x2=input('digite valor de x2: ')
y2=input('digite valor de y2: ')

if x1>n/2 and x2<n/2 or x1<n/2 and x2>n/2 or y1>n/2 and y2<n/2 or y1<n/2 and y2>n/2:
    print('S' )
else:
    print('N' )