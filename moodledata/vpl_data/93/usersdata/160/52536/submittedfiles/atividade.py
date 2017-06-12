# -*- coding: utf-8 -*-
import math

def coordenada(n):
    if x>=0 and y>=0 and ((x**2)+(y**2)<=1):
        return(True)
    else:
        return(False)
        
n=int(input('Digite a quantidade de coordenadas:'))
x=float(input('Digite a coordenada x:'))
y=float(input('Digite y:'))

if coordenada>=0 and coordenada>=0 and coordenada<=1:
    print('Sim')
else:
    print('Nao')
    
    
