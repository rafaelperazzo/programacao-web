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
print(soma)
        
        