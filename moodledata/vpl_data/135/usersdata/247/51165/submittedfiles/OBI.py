# -*- coding: utf-8 -*-
t=int(input('numero de competidores: '))
n=int(input('nota minima: '))
cont=0
for i range(1,n+1,1):
    x=int(input('nota 1: '))
    y=int(input('nota 2: '))
    if x+y>=n:
        cont=cont+1
print('cont')
    