# -*- coding: utf-8 -*-
n=int(input('Número de postos de água:'))
m=int(input('Distância intermediária máxima:'))
contador=0
x=0
for i in range (1,n+1,1):
    a=int(input('Distância do posto de água:'))
    b=a-x
    if b>m:
        contador=contador+1
    x=a
if contador==0:
    print('S')
else:
    print('N')