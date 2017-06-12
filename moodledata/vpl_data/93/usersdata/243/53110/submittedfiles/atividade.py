# -*- coding: utf-8 -*-
import math

def pontos(n):
    cont=0
    for i in range(1,n+1,1):
        if x>=0 and y>=0 and ((x*x)+(y*y))<=1:
            cont=cont+1
    if cont==0:    
        return(False)
    else:
        return(True)
        
n=int(input('digite a quantidade de pontos:'))
x=float(input('digite x:'))
y=float(input('digite y:'))

if pontos(n):
    print('SIM')
else:
    print('NAO')

