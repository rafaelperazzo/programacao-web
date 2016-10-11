# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n :')
x=input('Digite o valor da cordenada x:')
y=input('Digite o valor da cordenada y:')

while n>0:
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print('sim')
        
    else:
        print('não')
    
    n=n-1
    