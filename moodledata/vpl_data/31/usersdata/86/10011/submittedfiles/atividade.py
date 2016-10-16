# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('n:')
for i in range(1,n+1,1):
    x = int(input('x:'))
    y = int(input('y:'))
    if x>=0 and y>=0 and x**2+y**2<=1:
        print('SIM')
    else:
        print('NAO')