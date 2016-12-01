# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menorcoluna(lista):
    for j in range (0,lista.shape[1],1):
        for i in range (0,lista.shape[0],1):
            if lista[i,j]==1:
                return j
    
def maiorcoluna(lista):
    for j in range (0,lista.shape[1],1):
        for i in range (0,lista.shape[0],1):
            if lista[i,j]==1:
                cd=j
    return cd
    
def menorlinha(lista):
    for i in range (0,lista.shape[0],1):
        for j in range (0,a.shape[1],1):
            if lista[i,j]==1:
                return i
    
def maiorlinha(lista):
    for i in range (0,lista.shape[0],1):
        for j in range (0,lista.shape[1],1):
            if lista[i,j]==1:
                lb=j
    return lb
    
linhas=input('Digite o número de linhas:')
colunas=input('Digite o número de colunas:')

a=np.zeros ( (linhas , colunas) )

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')

print (a[menorlinha(a):maiorlinha(a)+1,menorcoluna(a):maiorcoluna(a)+1])
    
