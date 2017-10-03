# -*- coding: utf-8 -*-
import math
n=int(input('Digite o valor de n: '))
x=0
y=0
while (x<n) and (y<n):
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print('Sim')
    else:
        print('Nao')
    x=x+1
    y=y+1

    




