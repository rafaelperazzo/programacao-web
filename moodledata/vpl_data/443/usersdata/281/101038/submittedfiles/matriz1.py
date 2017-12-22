# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite a quantidade de linhas da matriz: '))
n=int(input('Digite a quantidade de colunas da matriz: '))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('Digite o %d termo: ' %(i+1))))
    matriz.append(linha)
print(matriz)
matrizt=[]

for i in range(m-1,-1,-1):
    linhat=[]
    for j in range(n-1,-1,-1):
        linhat.append(matriz[i][j])   
    matrizt.append(linhat)
print(matrizt)


