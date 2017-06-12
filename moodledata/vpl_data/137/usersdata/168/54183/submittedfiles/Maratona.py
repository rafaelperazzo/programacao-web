# -*- coding: utf-8 -*-
m=int(input('Digite o número de postos de água: '))
n=int(input('Digite a distância intermediária máxima de um atleta em metros: '))
j=m
cont=0
fo i in range(1,n+1,1):
    p=int(input('Digite a posição dos postos de água ao longo do trajeto: '))
    j=p-m
    if (j<m):
        cont=cont+1
if (cont!=n):
    print('N')
else:
    print('S')