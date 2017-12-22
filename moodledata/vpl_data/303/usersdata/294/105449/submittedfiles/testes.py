# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#AVENIDA

m= int(input('Digite a quantidade de linhas: '))
n= int(input('Digite a quantidade de colunas: '))
matriz= []
for i in range (0,m,1):
    linha= []
    for j in range (0,n,1):
        linha.append(int(input('Digite os elementos da linha%d: ' %(i+1))))
    matriz.append(linha)
menor=(100*m)+1
for j in range (0,n,1):
    soma=0
    for i in range (0,m,1):
        soma+=matriz[i][j]
    if soma<menor:
        menor=soma
print(menor)