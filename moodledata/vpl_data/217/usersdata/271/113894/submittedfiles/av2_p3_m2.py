# -*- coding: utf-8 -*-
import numpy as np
#ENTRADA
m = int(input('Digite a dimensão : '))
a = np.zeros((m,m))
for i in range (0,a.shape[0],1) :
    for j in range(0,a.shape[1],1) :
        a[i,j] = int(input('Digite o elemento : '))
        
#FUNÇÕES
def soma1 (matriz,linha) :
    soma = 0
    for i in range (0,matriz.shape[0],1) :
        for j in range (0,matriz.shape[1],1) :
            




