# -*- coding: utf-8 -*-
import math

n=int(input('Digite o valor de n:'))

while n>0:
    x=int(input('Digite o valor de x:'))
    y=int(input('Digite o valor de y:'))
    if x>=0 and y>=0 and ((x**2)+(y**2))<=1:
        print('Sim')
    else:
        print('NAO')
    n=n-1
