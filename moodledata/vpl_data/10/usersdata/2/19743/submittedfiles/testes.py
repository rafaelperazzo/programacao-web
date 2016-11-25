# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np

def soma(a,b): 
    c = np.zeros( (a.shape[0],a.shape[1]) )
    for i in range(0,c.shape[0],1):
        for j in range(0,c.shape[1],1):
            c[i,j] = a[i,j] + b[i,j]
    
    return c

#ESCREVER UM PROGRAMA EM PYTHON QUE FAÇA A SOMA DE 2 MATRIZES. MOSTRAR A MATRIZ C = A + B

#PASSO 1: PREPARAR E CRIAR AS MATRIZES. As matrizes possuem a mesma dimensão. 

linhas = input('Digite a quantidade de linhas: ')
colunas = input('Digite a quantidade de colunas: ')

a = np.zeros( (linhas,colunas) )
b = np.zeros( (linhas,colunas) )

#PASSO 2: Pedir para o usuário entrar com todos os elementos da(s) matriz(es)

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite um elemento para a: ')

for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j] = input('Digite um elemento para b: ')

#CALCULAR C = A + B
print soma(a,b)



