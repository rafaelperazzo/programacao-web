# -*- coding: utf-8 -*-
n=int(input('Digite o número de postos de água: '))
m=int(input('Digite a distância intermadiária máxima do atleta: '))
cont=0
for i in range (1, n+1, 1):
    d=int(input('Digite a posição do postos de água: '))
    d=d+m
    if (b<m):
        cont=cont+1
if (cont>1):
    print('S')
else:
    print('N')