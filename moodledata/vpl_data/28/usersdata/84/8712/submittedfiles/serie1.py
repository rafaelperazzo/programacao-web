# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite o valor de n:')
i=1
soma=0

while 1<=n:
    if i%2==0:
        soma=soma-(i/(i**2))
    else:
        soma=soma+(i/(i**2))
    i=i+1
print('%.5f'%soma)