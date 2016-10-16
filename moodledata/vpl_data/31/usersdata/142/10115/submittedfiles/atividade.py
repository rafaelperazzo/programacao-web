# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite um numero de repetiçoes n:')

for i in range (1,n+1,1):
    x=input('Digite x:')
    y=input('Digite y:')
    
    if x<0 or y<0:
        print ('não')
    if ((x**2)+(y**2))<=1:
        print ('sim')
    else:
        print ('não')