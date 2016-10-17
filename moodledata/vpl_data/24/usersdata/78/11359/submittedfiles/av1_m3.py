# -*- coding: utf-8 -*-
from __future__ import division
import math
m=int(input('digite o valor de m:'))

termo=0
soma=0
denominador=n*(n+1)*(n+2)

while termo<=m:
    if termo%2==0:
        soma=soma+(4/denominador)
    else:
        soma=soma+(4/denominador)
    termo=termo+1
    soma=soma+1
    n=n+1
pi=3+soma
print('%.6f'%pi)


