# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
a=1
j=((n//(10**a)))
while ((n//(10**a)))==1:
    print(a+1)
a=a+1