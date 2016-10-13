# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))

b=1
while n>0:
    if ((n//(10**b)))>1:
        print(b+1)
    b=b+1