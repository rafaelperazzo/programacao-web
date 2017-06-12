# -*- coding: utf-8 -*-
n=int(input('Número de postos de água: '))
m=int(input('Número da distância intermediária máxima de um atleta: '))
soma=0
cont=0
for i in range(1,n+1,1):
    p=int(input('Digite a posição: '))
    if p-m<0 or p-m==0 or p-m<=m:
        soma=soma+1
    p=novo
    if abs(novo-p)>m:
        cont=cont+1
if soma>0 and cont==0:
    print('S')
else:
    print('N')