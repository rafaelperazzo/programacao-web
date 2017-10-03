# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
x=float(input('Digite o valor de x: '))
y=float(input('Digite o valor de y: '))

while (x<n) and (y<n):
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print('Sim')
    else:
        print('Nao')
    x=x+1
    y=y+1

    




