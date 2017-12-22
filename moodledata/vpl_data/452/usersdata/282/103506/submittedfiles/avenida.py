# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite o valor de m: '))
n=int(input('Digite o valor de n: '))
while 2<=m and m<=1000:
    for i in range (0,m,1):
        linha=[]
        for j in range (0,n,1):
            linha.append(int(input('Digite um termo: ')))
        matriz.append(linha)
    print(matriz)
    break