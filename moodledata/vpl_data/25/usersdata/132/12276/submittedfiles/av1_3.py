# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
x=a
y=b
c=0
z=x%y
while (z!=0):
    c=c+1
    x=y
    y=z
print(c)    