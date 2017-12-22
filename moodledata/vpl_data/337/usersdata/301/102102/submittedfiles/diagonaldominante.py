# -*- coding: utf-8 -*-
n= int(input('Digite a ordem da matriz: '))
matriz= []
for i in range (0,n,1):
    linha= []
    for j in range (0,n,1):
        linha.append(int(input('Digite o elemento%d da matriz: ' %(i+1))))
    matriz.append(linha)


