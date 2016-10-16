# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de n:'))
i=0
n=0

if n<0:
    n*(-1)
for i in range (1,n+1,1):
    soma=0
    for j in range (1,n+1,1):
        i/((j-1)*(i-1))
soma=soma+1
print(soma)