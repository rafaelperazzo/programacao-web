# -*- coding: utf-8 -*-
from __future__ import division
import math
m=int(input('digite o valor de m:'))

termo=0
soma=0
n=2

while termo<=m:
    if termo%2==0:
        soma=soma+(4/n*(n+1)+(n+2))
    else:
        soma=soma-(4/(n+2)*(n+3)*(n+4))
    termo=termo+1
    soma=soma+1
    n=n+1
pi=3+soma
print('%.6f'%pi)


