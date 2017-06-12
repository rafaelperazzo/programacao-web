# -*- coding: utf-8 -*-
import math


n=int(input('digite o valor de n:'))

i=0
for i in range (1,n+1,1):
    x=float(input('Digite a coordenada x:'))
    y=float(input('digite a coordenada y:'))
    i=i+1
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print('SIM')
    else:
        print('NAO')