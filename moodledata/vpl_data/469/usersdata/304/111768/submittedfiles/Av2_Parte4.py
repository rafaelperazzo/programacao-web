# -*- coding: utf-8 -*-
m = int(input('Coluna: '))
n = int(input('Linha: '))
matriz = []
for i in range (0,n,1):
    linha=[]
    for j in range (0,m,1):
        linha.append(int(input('Linha: ')))
    matriz.append(linha)

soma = 0
for j in range (0,m,1):
    soma = matriz[i][0] + matriz[i][0]
for j in range (0,m,1):
    soma2 = matriz[i][1] + matriz[i][1]
for j in range (0,m,1):
    soma3 = matriz[i][2] + matriz[i][2]

if soma1>soma2:
    print(soma1)
elif soma1<soma2:
    print(soma2)
else:
    print(soma3)