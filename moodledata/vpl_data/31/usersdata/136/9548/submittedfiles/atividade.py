# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("digite n")
while n>0:
    x = input("valor de x")
    y = input("valor de y")
    
    
    if x>=0 and y >= 0 and (x**2)+(y**2)<=1:
        print('SIM')
    else:
        print('NAO')
    n = n-1
