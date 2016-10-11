# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite n: ')

i=0

while (i<=n):
    
    x=input('Digite x: ')
    y=input('Digite y: ')
    
    if (x>=0 and y>=0 and ((x**2)+(y**2))==0):
        print('SIM')
    else:
        print('NAO')
    i=i+1
    
    