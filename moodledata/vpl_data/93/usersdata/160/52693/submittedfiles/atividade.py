# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de coordenadas:'))

for i in range(1,n+1,1):
    x=float(input('Digite a coordenada x:'))
    y=float(input('Digite a coordenada y:'))

if x>=0:
    if y>=0:
        if (x**2)+(y**2)<=1:
            print('Sim')
else:
    print('Nao')
    


    
