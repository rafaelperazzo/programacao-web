# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
cont=0
while True:
    x=a//b
    cont=cont+1
    r=a%b
    a=b
    if r==0:
        break
    b=r
print(b)
print(cont)
