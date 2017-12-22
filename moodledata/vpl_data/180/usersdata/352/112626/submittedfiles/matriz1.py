# -*- coding: utf-8 -*-

import numpy as np

n=int(input('Numero de linhas: '))
m=int(input('Numero de colunas: '))
Ma=input('Digite a matriz: ')

A=np.fromstring(Ma, sep=' ').reshape(n,m)

def primeiralinha(A):
    for i in range (0,A.shape[0],1):
        for j in range (0,A.shape[1],1):
            if A[i,j]==1:
                return(i)


def ultimacoluna(A):
    for i in range(0,A.shape[0]-1,-1,-1):
        for j in range(0,A.shape[1]-1,-1,-1):
            if A[i,j]==1:
                return(i)

def primeiracoluna(A):
    for j in range(0,Ashape[1],1):
        for i in range(0,A.shape[0],1):
            if A[i,j]==1:
                return(j)


def ultimacoluna(A):
    for j in range(0,A.shape[1]-1,-1,-1):
        for i in range(0,A.shape[0]-1,-1,-1):
            if A[i,j]==1:
                return(j)
    
menorlinha=primeiralinha(A)
maiorlinha=ultimalinha(A)
menorcoluna=primeiracoluna(A)
maiorcoluna=ultimacoluna(A)


B=A[menorlinha:maiorlinha+1, menorcoluna:maiorcoluna+1]
print(B)






