# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('Digite o valor de :')
j=0
i=2
soma=3
while j<=M:
    if i%4==0:
        soma=soma+4/(i*(i+1)*(i+2))
    else:
        soma=soma-4/(i*(i+1)*(i+2))
    i=i+2
    j=j+1
print ('%.6f' %soma)