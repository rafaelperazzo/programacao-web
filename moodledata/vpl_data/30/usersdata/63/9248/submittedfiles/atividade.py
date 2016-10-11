# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite n:'))
if n<0:
    n*(-1)
cont=0
a=1
b=1

while n>=0:
    s=(a/n)+(a/(n-b))
    
cont=cont+1
a=a+1
b=b+1
print(s)    
     

   