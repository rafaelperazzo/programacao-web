# -*- coding: utf-8 -*-
from __future__ import division
import math
n=int(input('digite a quantidade de termos:'))
if n<0:
    n=n*-1
s=0
i=n
x=1
while(i>=1):
    y=x/i
    s=s+y
    i=i-1
    x=x+1
print('%.5f'%s)    
