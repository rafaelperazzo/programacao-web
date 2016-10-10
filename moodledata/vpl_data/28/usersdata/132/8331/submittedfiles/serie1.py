# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input(' digite o numero de termos:')
i=1
s=0
while(i<=a):
    x=(2*i-i)/(i**2)
    if i%2==0:
        s=s-x
    else:
        s=s+x
    i=i+1    
print(s)        