# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('digite o valor de m:')
p=2
q=3
r=4
soma=0
cont=1
while cont<=m:
    if cont%2==0:
        soma=soma-(4/(p*q*r))
    else:
        soma=soma+(4/(p*q*r))
    p=p+2
    q=q+2
    r=r+2
    soma=soma+3
print('%.6f'%soma)
