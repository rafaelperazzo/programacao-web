# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite A:')
b=input('Digite B:')
cont=0
while a%b!=0:
    c=b
    d=a%b
    a=c
    b=d
    cont=cont+1
print(b)
print(cont)