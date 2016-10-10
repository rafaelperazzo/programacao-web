# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('qtdd de divisores:')
a=input('n 1:')
b=input('n 2:')
i=1
c=0
while (c<n):
    if (i%a==0):
        print(i)
        c=c+1
    i=i+1