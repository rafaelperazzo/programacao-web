# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite o valor de n:'))
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=0
i=2
while c<n:
    if i%a==0 or i%b==0:
        print(i)
        c=c+1
    i=i+1
    