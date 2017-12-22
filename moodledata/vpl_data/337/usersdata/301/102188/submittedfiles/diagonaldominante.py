# -*- coding: utf-8 -*-
n= int(input('Digite a ordem da matriz: '))
matriz= []
for i in range (0,n,1):
    linha= []
    for j in range (0,n,1):
        linha.append(int(input('Digite o elemento%d da matriz: ' %(i+1))))
    matriz.append(linha)

for i in range(0,n,1):
    for j in range(0,n,1):
        if j<1:
        soma = matriz[i][i] + matriz[i][j+1] + matriz[i][j+2]
        soma-=matriz[i][i]
        if matriz[i][i]>soma:
            print('S')
        else:
            print('N')
