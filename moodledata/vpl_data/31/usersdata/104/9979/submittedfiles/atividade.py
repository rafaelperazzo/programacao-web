# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n:')
#PROCESSAMENTO+SAÍDA
for i in range(1,n+1,1):
    x=input('x:')
    y=input('y:')
    if (x**2)+(y**2)<=1 and y>=0 and x>=0:
        print('SIM')
    else:
        print('NAO')

