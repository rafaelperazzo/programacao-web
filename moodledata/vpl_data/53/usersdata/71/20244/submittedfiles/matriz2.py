# -*- coding: utf-8 -*-
from __future__ import division

#Entrada da Matriz
import numpy as np
n=input("Insira a Dimensão da Matriz: ")
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input("Insira o Elemento: ")
        
#Funções
def soma_diagonalP(matriz):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+matriz[i,i]
    return soma

def soma_diagonalS(matriz):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+matriz[i,(matriz.shape[0]-i-1)]
    return soma

def soma_linhas(matriz):
    soma=[]
    for i in range(0,matriz.shape[0],1):
        soma.append(sum(matriz[i,:]))
    return soma
    
def soma_linhas(matriz):
    soma=[]
    for i in range(0,matriz.shape[0],1):
        soma.append(sum(matriz[i,:]))
    return soma
    
def soma_coluna(matriz):
    soma=[]
    for i in range(0,matriz.shape[0],1):
        soma.append(sum(matriz[:,i]))
    return soma