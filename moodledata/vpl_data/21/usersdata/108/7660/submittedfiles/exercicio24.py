# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('Digite o valor de n:'))
m = int (input ('Digite o valor de m:'))
div=1
maior=0

if (n>=m):
    maior=n
else:
    maior=m
    
for i in range (1,maior+1, 1):
    if ((n%i==0) and (m%i==0)):
        div=i

print (div)
