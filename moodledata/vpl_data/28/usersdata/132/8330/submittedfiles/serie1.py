# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input(' digite o numero de termos:')
i=1
s=0
while(i<=a):
    x=4/(2*i-1)
    if i%2==0:
        s=s-x
    else:
        s=s+x
    i=i+1    
print(s)        