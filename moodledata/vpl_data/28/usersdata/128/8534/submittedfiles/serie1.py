# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite a quantidade de termos: ')

x=0
negativos=0
positivos=0

for i in range (1,n+1,1):
    x=i/(i**2)
    
    if i%2==0:
        negativos=negativos-x
    
    else:
        positivos=positivos+x
    
s=positivos+negativos

print ('%.5f') %s