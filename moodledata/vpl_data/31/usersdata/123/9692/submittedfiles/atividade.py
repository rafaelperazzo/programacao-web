# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input('Digite n:')
for i in range (0,n,1):
    x= input('Digite x:')
    y= input('Digite y:')
    if ((x**2)+(y**2))<=1 and x>=0 and y>=0:
        print ('SIM')
    if ((x**2)+(y**2))>1 or x<0 or y<0:
        print ('NÃO')