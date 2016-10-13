# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
a=1

while n>0:
    if (n//(10**a)<1):
        print(a+1)
    a=a+1