# -*- coding: utf-8 -*-
n=int(input('digite o numero de postos:'))
m=int(input('digite a distancia máxima do corredor:'))
mant=0
cont=1
for i in range(1,n+1,1):
    x=int(input('digite a distancia dos postos de agua:'))
    dis=x-mant
    if dis<=m:
        cont=cont+1
    mant=x
if cont==n:
    print('S')
else:
    print('N')