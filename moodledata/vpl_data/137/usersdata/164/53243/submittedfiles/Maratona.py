# -*- coding: utf-8 -*-
n=int(input('Digite o número de postos de água: '))
m=int(input('Digite a distância intermadiária máxima do atleta: '))
a=0
cont=0
for i in range (1, n+1, 1):
    d=int(input('Digite a posição do postos de água: '))
    a=a-d-m
    a=a*(-1)
    if (a<m):
        cont=cont+1
if (cont!=n):
    print('n')
else:
    print('s')