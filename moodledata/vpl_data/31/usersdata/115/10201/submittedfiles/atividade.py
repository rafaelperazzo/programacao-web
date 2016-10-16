# -*- coding: utf-8 -*-
from __future__ import division
import math

N=input('Digite o N:')

for i in range (0, N, 1):
    x=input('Digite o x:')
    y=input('Digite o y:')
    if((x**2)+(y**2))<=1 and x>=0 and y>=0:
        print('SIM')
    else:
        print('NÂO')
