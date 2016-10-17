# -*- coding: utf-8 -*-
from __future__ import division
import math

m= input('Digite o valor de m:')

i=1
den=2
soma=3
while (i<=m):
    if (i%2==0):
        soma= soma - 4/(den*(den+1)*(den+2))
    else:
        soma= soma + 4/(den*(den+1)*(den+2))
        
    den=den+2
    i=i+1
print ('%.6f' %soma)
