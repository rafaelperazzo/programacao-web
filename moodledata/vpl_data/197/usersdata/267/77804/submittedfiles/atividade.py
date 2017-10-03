# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
for i in range (1,n+1,1):
    x=float(input('Valor de x: '))
    y=float(input('Valor de y: '))
    if x>=0 and y>=0 and (x*x + y*y)<=1:
        print('SIM')
    else:
        print('NAO')

