# -*- coding: utf-8 -*-
from __future__ import division
import math
m=int(input('digite o valor de m:'))

termo=2
soma=0
n=1

while termo<=m:
    if termo%2==0:
        soma=soma+(4/n*(n+1)*(n+2))
    else:
        soma=soma-(4/n*(n+1)*(n+2))
    termo=termo+1
    soma=soma+1
    n=n+1
soma=3+soma
print('%.6f'%soma)


