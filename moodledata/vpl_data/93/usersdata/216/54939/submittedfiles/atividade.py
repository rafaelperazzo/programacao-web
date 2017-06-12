# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade:'))

def pontos(x,y):
    for i in range(1,n+1,1):
        if (x>=0) and (y>=0) and (((x**2)+(y**2))<=1):
            return True
        else:
            return False

x=float(input('Digite x:'))
y=float(input('Digite y:'))

if (pontos(x,y)):
    print('SIM')
else:
    print('NAO')

