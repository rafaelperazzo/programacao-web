# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('digite o valor de m:')
i=1
j=2
soma=0
for i in range(1,m+1,1):
     if i%2==0:
        soma=soma-4/(j*(j+1)*(j+2))
    else:
        soma=soma+4/(j*(j+3)*(j+4))
    i=i+1
    J=j+1
soma=soma+3

print(soma)
