# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de coordenadas:'))
x=int(input('Digite a coordenada x:'))
y=int(input('Digite y:'))

if x>=0 and y>=0 and ((x**2)+(y**2)<=1):
    print('Sim')
else:
    print('Nao')
    
    
