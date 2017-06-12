# -*- coding: utf-8 -*-
import math
n=int(input('quantidade de pontos:'))
for i in range(1,n+1,1):
    x=float(input('cordenadas x:'))
    y=float(input('cordenadas y:'))
    if ((x**2)+(y**2))<=1:
        print('SIM')
    else:
        print('NAO')