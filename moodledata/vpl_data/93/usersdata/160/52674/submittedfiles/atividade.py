# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de coordenadas:'))

i=0
for i in range(0,n+1,1):
    x=float(input('Digite a coordenada x:'))
    y=float(input('Digite y:'))
if (x>=0) and( y>=0) and ((x**2)+(y**2)<=1):
    print('Sim')
else:
    print('Nao')
    


    
