# -*- coding: utf-8 -*-
from __future__ import division

#Entrada da Matriz
import numpy as np
linhas=input("Insira o Número de Linhas: ")
colunas=input("Insira o Número de Colunas: ")
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input("Insira o Elemento: ")
        
#Funções
def coluna_esquerda(a):
    ce=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            ce=i
            break
    return ce
    
def coluna_direita(a):
    cd=0
    for i in range(0,a.shape[0],1):
        if 1 in a[:,i]:
            cd=i
    return cd    
    
def linha_superior(a):
    ls=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            ls=i
            break
    return ls
    
def linha_inferior(a):
    li=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            li=i
    return li