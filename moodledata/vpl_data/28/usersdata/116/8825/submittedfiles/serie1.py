# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input ('insira o valor de n:')

cont=0
i=1
while i<=n:
    if i%2==0:
        cont = cont-(i/(i**2))
    else:
        cont = cont+(i/(i**2))
    i=i+1
print ('%.5f' %cont)