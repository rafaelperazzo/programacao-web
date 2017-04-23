# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n:'))
contador=1
while contador<=n:
    a=float(input('digite o valor de a:'))
    b=float(input('digite o valor de b:'))
    if a>=0 and b>=0 and ((a**2)+(b**2))<=1:
        print('SIM')
    else:
        print('não')
    contador=contador+1    

