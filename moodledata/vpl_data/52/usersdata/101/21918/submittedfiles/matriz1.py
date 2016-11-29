# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Coluna da Direita
def maior_coluna(a):
    for j in range (0, a.shape[1], 1):
        for i in range (0, shape[0], 1):
            if a[i,j] == 1:
                cd = j
    return cd
                
#Coluna da Esquerda
def maior_coluna(a):
    for j in range (0, a.shape[1], 1):
        for i in range (0, shape[0], 1):
            if a[i,j] == 1:
                return j
                
#Linha de Baixo
def maior_linha(a):
    for i in range (0, a.shape[0], 1:):
        for j in range (0, a.shape[1], 1):
            if a[i,j] == 1:
                lb = i 
    return lb

#Linha de Cima
def maior_linha(a):
    for i in range (0, a.shape[0], 1:):
        for j in range (0, a.shape[1], 1:):
            if a[i,j] == 1:
                return i

linhas = input('Digite a quantidade de linhas: ')
colunas = input('Digite a quantidade de colunas: ')

a = np.zeros((linhas,colunas))

for i in range (0, a.shape[0], 1):
    for j in range (0, a.shape[1], 1):
        a[i,j] = input('Digite qualquer elemento: ')
        

print (a[menor_linha(a):maior_linha(a)+1, menor_coluna(a):maior_coluna(a)+1])










