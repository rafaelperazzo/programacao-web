# -*- coding: utf-8 -*-
n=int(input('digite o numero de postos:'))
p=int(input('digite a distancia maxima do alteta:'))
for i in range(1,n+1,1):
    x=int(input('digite a distancia entre os postos de agua:'))
    x=x-p
if x<=p:
    print('S')
else:
    print('N')