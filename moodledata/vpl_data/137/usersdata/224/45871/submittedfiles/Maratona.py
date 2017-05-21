# -*- coding: utf-8 -*-
n=int(input('Número de postos de água: '))
m=int(input('Número da distância intermediária máxima de um atleta: '))
soma=0
p=0
for i in range(1,n+1,1):
    p=int(input('Posição: '))
    if p-m<=0 or p-m==m:
        soma=soma+1
    p=p+1
if soma==0:
    print('S')
else:
    print('N')