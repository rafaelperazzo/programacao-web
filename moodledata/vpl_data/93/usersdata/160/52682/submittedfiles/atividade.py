# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de coordenadas:'))

i=0
for i in range(0,n,1):
    x=float(input('Digite a coordenada:'))
    y=float(input('Digite a coordenada:'))
    
if x>=0:
    if y>=0:
        if (((x*x)+(y*y))<=1):
            print('Sim')
else:
    print('Nao')
    


    
