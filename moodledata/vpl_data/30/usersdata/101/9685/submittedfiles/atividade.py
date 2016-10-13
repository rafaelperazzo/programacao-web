# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('digite o valor de n: '))
cont = 0
if n<0:
    n = n*(-1)
for i in range (1,n+1,1):
    cont = cont + (i/n)
    i= +1
    n = n-1
print ('%.5f' %cont)