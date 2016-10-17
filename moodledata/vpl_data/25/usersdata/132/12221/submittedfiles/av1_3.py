# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
x=a
y=b
x%y
c=0
while True:
    if x%y!=0:
        c=c+1
    if x%y==0:
        break
    x=y
    y=z
print(c)    