# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('digite o valor de n'))

if n<0:
    n=n*(-1)
S=(1/n+2/(n-1)+3/(n-2)+...+n/1)

print('S=%.5f'%S)




