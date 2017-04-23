# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n:'))
contador=1
while contador<=n:
    x=float(input('Digite o valor de x:'))
    y=float(input('Digite o valor de y:'))
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print('SIM')
    else:
        print('NAO')
    contador=contador+1