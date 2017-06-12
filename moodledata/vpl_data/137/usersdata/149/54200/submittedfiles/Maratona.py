# -*- coding: utf-8 -*-
n=int(input('digite o número de postos de água:'))
m=int(input('digite a distancia máxima:'))
j=m
cont=0
for i in range(1,n+1,1):
    p=int(input('digite a posição dos postos ao longo do caminho:'))
    j=p-m
    if (j<m):
        cont=cont+1
if (cont!=n):
    print('N')
else:
    print('S')