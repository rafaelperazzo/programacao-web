# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Funções
def colunaEsquerda(a):
    Esquerda = 0
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j] == 1:
                Esquerda = j
                break
    return Esquerda

def colunaDireita(a):
    Direita = a.shape[1] -1
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j] == 1:
                Direita = j
    return Direita

def linhaCima(a):
    LC = 0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j] == 1:
                LC = i
                break
    return LC
    
def linhaBaixo(a):
    LB = a.shape[0]-1
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j] == 1:
                LB = i
    return LB
    
#CódigoPrincipal
linhas = input ('Digite a quantidade de linhas:')
colunas = input ('Digite a quantidade de colunas:')
a= np.zeros ((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input ('Digite um número:')
print (a[linhaCima(a):(linhaBaixo(a)+1),colunaEsquerda(a):(colunaDireita(a)+1)])