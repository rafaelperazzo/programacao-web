# -*- coding: utf-8 -*-
import math

i = 1
n= int(input('digite o valor de n: '))

while (i<=n):
    x = float(input('digite o valor de x: '))
    y = float(input('digite o valor de y: '))
    if (x>=0) and (y>=0) and (((x**2)+(y**2))<=1):
        print ('sim')
    else:
        print('nao')
    i = i+1
    
    
