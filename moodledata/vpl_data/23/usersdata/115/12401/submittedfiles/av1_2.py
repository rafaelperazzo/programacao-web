# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite o valor de n:')
x1=input('digite o valor de x1:')
y1=input('digite o valor de y1:')
x2=input('digite o valor de x2:')
y2=input('digite o valor de y2:')
z=n/2
if  x1<=z and y1<=z or x2>=z or y2>=z:
    print('S')
elif x2<=z and y2<=z or x1>=z or y1>=z:
    print('S')
else:
    print('N')