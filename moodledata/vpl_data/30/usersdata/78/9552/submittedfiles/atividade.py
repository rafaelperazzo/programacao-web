# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('digite o valor de n:'))
if n<0:
    n=n*(-1)

i=1
j=n
soma=0
while i<=n:
    soma=soma+(i/j)
    i=i+1
    j=j-1
prnt('%.5f'%soma)


