# -*- coding: utf-8 -*-
import math
n=int(input('digite o numero de pontos: '))
x=float(input('digite o x: '))
y=float(input('digite o y: '))

while (x<n):
    if (x>=0) and (y>=0) and (((x*x)+(y*y))<=1):
        print('SIM')
    else:
        print('NAO')
    x=x+1
    y=y+1


