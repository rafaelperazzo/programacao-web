# -*- coding: utf-8 -*-
from __future__ import division
import math
n = input ('digite o valor de n:')
for i in range (0,n,1):
    x = input ('x')
    y = input ('y')
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print ('sim')
    else:
        print ('não')

