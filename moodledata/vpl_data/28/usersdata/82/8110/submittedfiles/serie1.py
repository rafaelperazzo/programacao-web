# -*- coding: utf-8 -*-
from __future__ import division
import math
n = input('Digite o valor de n:')
i=1
j=1
soma=0
while i<=n:
    if (i%2==0):
        soma=soma-(j/(j**2))
    else:
        soma=soma+(j/(j**2))
    
    i=i+1
    j=j**2
print ('%.5f' %soma)
