# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite n:'))
if n<0:
    n*(-1)
cont=0
i=1
j=n

while i<=n:

    cont=cont+(i/j)
    i=i+1
    j=j-1
print('%.5f '%cont)    
     

   