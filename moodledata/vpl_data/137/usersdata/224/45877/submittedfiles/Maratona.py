# -*- coding: utf-8 -*-
n=int(input('Número de postos de água: '))
m=int(input('Número da distância intermediária máxima de um atleta: '))
soma=0
p=temp
for i in range(1,n+1,1):
    p=int(input('Digite a posição: '))
    if p-m>0 or p-temp>0:
        soma=soma+1
        p=temp
if soma>0:
    print('N')
else:
    priint('S')