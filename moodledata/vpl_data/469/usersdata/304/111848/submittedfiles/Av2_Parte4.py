# -*- coding: utf-8 -*-
m = int(input('Coluna: '))
n = int(input('Linha: '))
matriz = []
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input('Linha: ')))
    matriz.append(linha)
print(matriz)

soma1 = 0
soma2 = 0
soma3 = 0
for j in range (0,m,1):
    soma1 = soma1 + matriz[i][0]+matriz[i][0]
for j in range (0,m,1):
    soma2 = soma2 + matriz[i][1]+matriz[i][0]
for j in range (0,m,1):
    soma3 = soma3 + matriz[i][2]+matriz[i][0]

if soma1<soma2 and soma1<soma3:
    print(soma1)
if soma2<soma1 and soma2<soma3:
    print(soma2)
if soma3<soma1 and soma3<soma2:
    print(soma1)