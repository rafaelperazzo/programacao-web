# -*- coding: utf-8 -*-
import math


def pontos(n):
    cont=0
    for i in range(1,n+1,1):
        if x>=0 and y>=0 and (x**2)+(y**2)<=1:
            cont=cont+1
                     
    if cont==0:
        return(False)
    else:
        return(True)
n=int(input('Digite a quantidade de coordenadas:'))
for i in range(1,n+1,1):
    x=float(input('Digite a coordenada x:'))
    y=float(input('Digite a coordenada y:'))

if pontos(n):
    print('Sim')
else:
    print('Nao')


    
