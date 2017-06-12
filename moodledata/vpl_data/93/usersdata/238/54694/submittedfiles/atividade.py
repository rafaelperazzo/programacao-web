# -*- coding: utf-8 -*-
import math
n=int(input('digite um numero:'))

def region(x,y):
    if(x>=0) and (y>=0) and (x**2+y**2<=1):
        return true
    else:
        return false
for i in range (n):
    x=float(input('digite a coordenada de x:'))
    y=float(input('digite a coordenada de y:'))
    if region(x,y)==true:
        print('sim')
    else:
        ('nao')
