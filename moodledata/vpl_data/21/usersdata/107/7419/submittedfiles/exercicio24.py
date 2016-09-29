# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
i=1
g=0
if a>=b:
    while i<=a:
        if a%i==0 and b%i==0:
            g=i
        i=i+1   
if b>a:
    while i<=b:
        if a%i==0 and b%i==0:
            g=i
        i=i+1
print g