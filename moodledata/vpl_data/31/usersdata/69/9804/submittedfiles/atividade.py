# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite o valor de n:')
for i in range (0,n,1):
    x=input('digite o valor de x:')
    y=input('digite o valor de y:')
    if x>=0 and y>=0 and (((x*x)+(y*y))<=1):
        print ('SIM')
    else:
        print ('NAO')
