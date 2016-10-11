# -*- coding: utf-8 -*-
from __future__ import division
import math
#entrada 
n=input('digite o valor de n:')

#processamento e saida 
for i in range (1,n+1,1):
    x=input('digite o valor de x:')
    y=input('digite o valor de y:')
    if x>=0 and y>=0 and x**2+y**2<=1:
        print('sim')
    else :
        print('nao')
    
