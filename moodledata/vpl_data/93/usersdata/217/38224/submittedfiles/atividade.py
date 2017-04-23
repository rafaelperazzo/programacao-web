# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
contador=1
while contador<=n:
    x=float(input('digite x:'))
    y=float(input('digite y:'))
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print(SIM)
    else:
        print(NAO)
    contador=contador+1
    
