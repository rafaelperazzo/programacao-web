# -*- coding: utf-8 -*-
def pesoDaPosicao(matriz,linha,coluna):
    somaDaLinha=0
    somaDaColuna=0
    for i in range(0,matriz.shape[0],1):
        for j in range(0,matriz.shape[1],1):
            if i==linha:
                somaDaLinha=somaDaLinha+matriz[i,j]
            if j==coluna:
                somaDaColuna=somaDaColuna+matriz[i,j]
    total=somaDaLinha+somaDaColuna-(matriz[linha,coluna]*2)
    return (total)

import numpy as np
n=int(input('Informe a quantidade de linhas e colunas da matriz: '))
matriz=np.zeros((n,n))

linha=int(input('Informe o índice da linha da torre: '))
coluna=int(input('Informe o índice da coluna da torre: '))

for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Informe os elementos da matriz: '))

resultado=pesoDaPosicao(matriz,linha,coluna)
print('%.d'%resultado)
