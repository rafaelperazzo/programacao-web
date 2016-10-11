# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('digite o valor de n:')

if n>0:
    n=n*(-1)
cont=0
for i in range (1,n+1,1):
    cont=cont+(i/n)
    i=i+1
    n=n-1
    
print ('cont=%.5f'%cpnt)
