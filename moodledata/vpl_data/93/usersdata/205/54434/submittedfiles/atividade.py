# -*- coding: utf-8 -*-
import math
n=int(input('digite o valor de n:'))

def region (x,y):
    if (x>=0) and (y>=0) and (x**2+y**2<=1):
        return True
    else:
        return False
for i in range (n):
    x=float(input('digite o valor de x:'))
    y=float(input('digite o valor de y:'))
    if region (x,y)==True:
        print('sim')
    else:
        print('não')
    


