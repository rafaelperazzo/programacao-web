# -*- coding: utf-8 -*-
from __future__ import division
import math

m= input('Digite o valor de m:')

i=1
den=2
soma=0
while (i<=m):
    soma=soma + (4/(den*(den+1)*(den+2)))+3
    den=den+2
print ('%.6f' %soma)
