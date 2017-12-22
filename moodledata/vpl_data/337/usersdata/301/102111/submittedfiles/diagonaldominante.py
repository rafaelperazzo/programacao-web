# -*- coding: utf-8 -*-
n= int(input('Digite a ordem da matriz: '))
matriz= []
for i in range (0,n,1):
    linha= []
    for j in range (0,n,1):
        linha.append(int(input('Digite o elemento%d da matriz: ' %(i+1))))
    matriz.append(linha)

for j in range(0,n,1):
    for i in range(0,n,1):
        if i==j :
            if matriz[i][j]== (matriz[i][j+1]) + (matriz[i][j+2]):
                print('S')
            else:
                print('N')
