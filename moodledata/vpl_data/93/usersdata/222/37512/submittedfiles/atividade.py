# -*- coding: utf-8 -*-
import math
n=float(input('n:'))
x=float(input('x:'))
y=float(input('y:'))
soma=0
i=1
for i in range(1,n+1,1):
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
         print('SIM')
         soma=soma+1
else:
    print('NAO')



