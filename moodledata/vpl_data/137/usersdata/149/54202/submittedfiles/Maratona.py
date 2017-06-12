# -*- coding: utf-8 -*-
a=int(input('digite o número de postos de água:'))
b=int(input('digite a distancia máxima:'))
k=b
cont=0
for i in range(1,a+1,1):
    p=int(input('digite a posição dos postos ao longo do caminho:'))
    k=p-b
    if (k<b):
        cont=cont+1
if (cont!=a):
    print('N')
else:
    print('S')