# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('o primeiro numero: ')
b=input('o segundo numero: ')
i=1
c=b
if b>a:
    b=a
    a=c
while a%b!=0:
    c=a
    a=b
    b=c%b
    i=i+1
print(b)
print(i)
