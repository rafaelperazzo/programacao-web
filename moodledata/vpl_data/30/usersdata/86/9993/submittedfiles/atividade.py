# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('n:'))
soma = 0 
if n<0:
    n=n*(-1)
for i in range(1,n+1,1):
    soma=soma+i/n
    n=n-1
print("%.5f"%soma)


