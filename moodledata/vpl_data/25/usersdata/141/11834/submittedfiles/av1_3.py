# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('digite o valor de a:')
b=input('digite o valor de b:')
cont=0
while b>0:
    b=a%b
    cont=cont+1
print(b)
print(cont)
