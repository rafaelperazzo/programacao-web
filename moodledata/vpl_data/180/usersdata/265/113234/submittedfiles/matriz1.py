# -*- coding: utf-8 -*-
import numpy as np

linhas = int(input('digite a quantidade de linhas: '))
colunas = int(input('digite a quantidade de colunas: '))

a = np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o elemento: '))
        
def soma_liha(b,1):
    soma=0
    for j in range(0,b.shape[1],1):
        soma=soma+b[1,j]
    return(soma)
    
def soma_coluna(b,c):
    soma=0
    for i in range(0,b.shape[0],1):
        soma=soma+b[i,c]
    return(soma)
    
