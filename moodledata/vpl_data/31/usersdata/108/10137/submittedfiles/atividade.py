# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('Digite n:'))
i=1

while (i<=n):
    x = int (input ('x:'))
    y = int (input ('y:'))
    
    if((x>=0) and (y>=0)):
        fx=0
        fx=(x**2)+(y**2)
        if (fx<=1):
            print ('S')
        else:
            print ('N')
    else: 
        print ('N')
i=i+1