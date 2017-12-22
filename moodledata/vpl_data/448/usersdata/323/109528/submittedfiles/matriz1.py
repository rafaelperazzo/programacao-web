# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de linhas da matriz: '))
n=int(input('Digite a quantidade de colunas da matriz: '))

import copy
def rotacionar(matriz, grau):
    nova_matriz=copy.deepcopy(matriz)
    for i in range(len(matriz)):
        if grau==180:
            nova_matriz[len(matriz)-(i+1)]
            [len(matriz)-(j+1)=matriz[i][j]
    return nova_matriz



