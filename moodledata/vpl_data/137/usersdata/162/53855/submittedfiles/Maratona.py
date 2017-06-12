# -*- coding: utf-8 -*-
n=int(input('Número de postos de água:'))
m=int(input('Número da distância intermediária máxima de um atleta:'))
soma=0
a=0
for i in range(1,n+1,1):
    p=int(input('Digite a posição:'))
    if (p-a)<=m:
        soma=soma+1
    a=p
if soma==n:
    print('S')
else:
    print('N')