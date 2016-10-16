# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite o valor de n:')
j=n
soma=0
for i in range(0,n,1):
    j=j-1
    soma=soma+(i/j)
print(soma)