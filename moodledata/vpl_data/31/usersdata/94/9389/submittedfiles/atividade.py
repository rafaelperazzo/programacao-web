# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite o valor de n:')
wile n>0:
    x=input('digite o x:')
    y=input('digite o y:')
    if x>=0 and y>=0 and ((x**2)-(y**2))<=1:
        print('SIM')
    else:
        print('NÃO')
    n=n-1
    