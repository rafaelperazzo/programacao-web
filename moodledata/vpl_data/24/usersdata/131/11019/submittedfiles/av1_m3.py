# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('digite o valor de m:')
soma=0
termo=1 
while termo<=m:
    n1 = 2*termo
    n2 = 2*termo+1
    n3 = 2*termo+2
    denominador=n1*n2*n3
    if termo %2==0:
        soma=(soma-(4/denominador))
    else:
        soma=(soma+(4/denominador))
    termo=termo+1
pi = 3 +soma
print('%.6f' %pi)