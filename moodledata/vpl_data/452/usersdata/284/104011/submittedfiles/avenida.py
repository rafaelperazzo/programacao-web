# -*- coding: utf-8 -*-
matriz=[]
m=int(input('casa na horizontal: '))
n=int(input('casa na vertical: '))
for i in range(0,m,1):
    bairro=[]
    for j in range(0,n,1):
        bairro.append(int(input('valor da casa: ')))
    matriz.append(bairro)
print(matriz)

soma_coluna=[]
for j in range(0,n,1):
    soma=0
    for i in range(0,m,1):
        soma+=matriz[i][j]
    soma_coluna.append(soma)
for i in range(0,m-1,1):
    if soma_coluna[i]<=soma_coluna[i+1]:
        print(soma_coluna)
        
print(soma_coluna)

        
        