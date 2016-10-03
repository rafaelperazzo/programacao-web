# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('Digite o número de termos:'))
somatorio=0

for i in range (1,n+1,1):
    if (i%2!=0):
        somatorio = somatorio + (i/(i**2))
    else:
        somatorio = somatorio - (i/(i**2))
        
print (somatorio)
    