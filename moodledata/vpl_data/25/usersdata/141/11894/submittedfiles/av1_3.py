# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
cont=0
while b>0:
    x=a//b
    cont=cont+1
    b=a%b
    a=a//x
print(b)
print(cont)
