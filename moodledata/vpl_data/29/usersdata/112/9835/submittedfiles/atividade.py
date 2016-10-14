# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
if n<0:
    n=n*(-1)
b=1
if n<10:
    print(1)
while n>0:
    
    if ((n//(10**b)))>0:

    b=b+1
print(b)