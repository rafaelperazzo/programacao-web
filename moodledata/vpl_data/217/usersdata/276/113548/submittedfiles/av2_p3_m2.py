# -*- coding: utf-8 -*-
import numpy as np

n = int (input ('Digite a dimensão do quadrado mágico: '))

while n<3:
    n = int (input('Digite a dimensão do quadrado mágico: '))

matriz = np.zeros ((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i,j] = int (input ('Digite os elementos do quadrado mágico: '))

def somalinha (matriz):
    for i in range (0,matriz.shape[0],1) :
        for j in range (0,matriz.shape[1],1):
            somalinha = somalinha + a[i,j]
        