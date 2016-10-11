# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite n:'))
if n<0:
    n*(-1)
cont=0
a=1
b=n

while a<=n:
    n=(a/n)+(a/(n-b))

    cont=cont+(a/b)
    a=a+1
    b=b-1
print('%.5f '%cont)    
     

   