# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite um numero: '))
if n<0:
    n=n*(-1)
soma=0

for i in range(1,n+1,1):
    soma=soma+(i/n)
    i=i+1
    n=n-1
print ('%.5f' %soma)
