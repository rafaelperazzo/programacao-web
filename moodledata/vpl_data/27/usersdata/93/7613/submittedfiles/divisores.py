# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('n:')
a=input('a:')
b=input('b:')
for i in range(1,n+1,1):
    if i%a==0 or i%b==0:
        print (i)
    
