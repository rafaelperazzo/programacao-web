# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))
if n<0:
    n=n*(-1)
soma=0

for i in range(1,n+1,1):
    soma=soma+(i/n)
    n= n-1
    i=i+1
print(soma)

