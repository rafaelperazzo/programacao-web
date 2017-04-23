# -*- coding: utf-8 -*-
import math
n=int(input('digite o números de pontos que vc deseja avaliar:'))
for cont range (1,n+1,1):
    x=float(input('digite o valor da cordenada X:'))
    y=float(input('digite o valor da abcissa Y:'))
    if (x>=0) and (y>=0) and (((x*x)+(y*y))<=1):
        print('x=%.f'%x)
        print('y=%.f'%y)
        print('SIM')
    else:
        print('x=%.f'%x)
        print('y=%.f'%y)
        print('NAO')
    

