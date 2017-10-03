# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de pontos: '))
i=0
while (i<n):
    x=float(input('digite o x: '))
    y=float(input('digite o y: '))
    if (x>=0) and (y>=0) and (((x**2)+(y**2))<=1):
        print('SIM')
    else:
        print('NAO')
    i=i+1
    


