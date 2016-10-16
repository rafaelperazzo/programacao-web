# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite o valor de n:')
x=input('digite a coordenada x:')
y=input('digite a coordenada y:')
if (x>=0) and (y>=0) and ((x**2)+(y**2)<=1):
    print('S')
else:
    print('N')
