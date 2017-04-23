# -*- coding: utf-8 -*-
import math
n=int(input('digite n'))
cont=1
while cont<=n:
    x=float(input('digite x: '))
    y=float(input('digite y: '))
    
    if x>=0 and y>=0 and (x*x)+(y*y)<=1:
        print('SIM')
    else:
        print('NAO')
    
    cont=cont+1    

