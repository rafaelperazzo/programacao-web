# -*- coding: utf-8 -*-
import math
n=int(input('Digite o número de pontos:'))
for i in range (1,n+1,1):
    x=float(input('Digite o valor da coordenada x:'))
    y=float(input('Digite o valor da abcissa y:'))
    if x>=0 and y>=0 and (x**2+y**2<=1):
        print('SIM')
    else:
        print('NAO')