# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('Digite o valor de m:')
pi=3
j=4
l=2
for i in range (1,m+1,1):
    if i%2==0:
        pi=pi-4/(j*(j+1)*(j+2))
    else:
        pi=pi+4/(l*(l+1)*(l+2))
    j=j+2
    l=l+2
print ('o valor de pi é' 6%pi)