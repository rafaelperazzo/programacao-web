# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('o primeiro numero: ')
b=input('o segundo numero: ')
i=0
while a%b!=0:
    a=b
    b=a%b
    i=i+1
print(b)
print(i)
