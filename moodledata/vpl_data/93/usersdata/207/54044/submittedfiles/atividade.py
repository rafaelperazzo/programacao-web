# -*- coding: utf-8 -*-
import math
n=int(input('escreva n:'))

for i in range(0,n,1):
    x=float(input('escreva x:'))
    y=float(input('escreva y:'))
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print('sim')
    else:
        print('nao')


