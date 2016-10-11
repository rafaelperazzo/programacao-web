# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('digite o valor de n:')

while n>0:
    x=input('valor da coordenada x:')
    y=input('valor da coordenada y:')
    
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print('sim')
        
    else:
        print('nao')
    n=n-1