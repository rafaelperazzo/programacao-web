# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite o valor de n:')

while n>0:
    x=input('digite x:')
    y=input('digite y:')
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print ('Sim')
    else:
        print ('Não')
    n=n+1