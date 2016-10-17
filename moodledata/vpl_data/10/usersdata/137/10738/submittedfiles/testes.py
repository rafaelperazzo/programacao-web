# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite n:'))
soma=0
for i in range (0,n+1,1):
    a=int(input('a:'))
    if a>=0:
        soma+=i
        
        print soma
    else:
        break
    
   