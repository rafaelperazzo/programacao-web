# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de termos: ')
s=0
for i in range(1,n+1,1):
    v=i/(i**2)
    if i%2==0:
        s=s-v
    else:
        s=s+v
print('%5.f' %s)
