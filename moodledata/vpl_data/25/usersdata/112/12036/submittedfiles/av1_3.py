# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a')
b=input('Digite o valor de b')
c=a%b
while a%b!=0:
    if c==a%b and c!=0:
        a=b
        b=c
    d=c
print(c)
    