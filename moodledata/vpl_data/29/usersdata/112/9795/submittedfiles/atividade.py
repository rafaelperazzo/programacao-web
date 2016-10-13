# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))

b=1
while n>0:
    if n<10:
        print(1)
    if ((n//(10**b)))>0:
        print(b+1)
    b=b+1