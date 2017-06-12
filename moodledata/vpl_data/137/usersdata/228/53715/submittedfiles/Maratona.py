# -*- coding: utf-8 -*-
n=int(input('digite o numero de pontos:'))
dmi=float(input('digite a distancia media intermediaria:'))
y=0
for i in range(1,n+1,1):
    p=float(input('digite a posição do posto'))
    x=p
    distancia=abs(x-y)
    if dmi>distancia:
        print('S')
    else:
        print('N')
    y=p    




