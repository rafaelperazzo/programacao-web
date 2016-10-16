# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite o valor de n:')
if n<0:
    n=n*(-1)
j=n
soma=0
for i in range(1,n+1,1):
    if j==0:
        break
    soma=soma+(i/j)
    j=j-1
print(soma)