# -*- coding: utf-8 -*-
import math

def pontos(n):
    if x>=0 and y>=0 and ((x*x)+(y*y))<=1:
        return(True)
    else:
        return(False)
        
n=int(input('digite a quantidade de pontos:'))
x=float(input('digite x:'))
y=float(input('digite y:'))

if pontos(n):
    print('SIM')
else:
    print('NAO')

