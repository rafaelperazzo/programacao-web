# -*- coding: utf-8 -*-
import math
n=int(input('n:'))
x=int(input('x:'))
y=int(input('y:'))
i=1
for i in range(1,n+1,1):
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
         print('SIM')
else:
    print('NAO')



