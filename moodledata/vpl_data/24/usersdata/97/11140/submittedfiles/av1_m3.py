# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('digite o valor de m:')
i=1
j=2
while i<=m:
     if i%2==0:
        soma=soma-4/(j*(j+1)*(j+2))
    else:
        soma=soma+4/(j*(j+3)*(j+4))
    i=i+1
    J=j+1
soma=soma+3

print('%.6f'%soma)
