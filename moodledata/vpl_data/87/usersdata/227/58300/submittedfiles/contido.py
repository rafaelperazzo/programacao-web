# -*- coding: utf-8 -*-
import math
n=int(input('Quantidade de pontos:'))
for i in range(1,n+1,1):
    x=float(input('Cordenadas x:'))
    y=float(input('Cordenadas y:'))
    if ((x**2)+(y**2))<=1:
        print('SIM')
    else:
        print('NAO')