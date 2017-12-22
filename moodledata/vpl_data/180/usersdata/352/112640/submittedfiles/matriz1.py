# -*- coding: utf-8 -*-

import numpy as np



#A=np.fromstring(Ma, sep=' ').reshape(n, m)

def primeiralinha(A):
    for i in range (0,A.shape[0],1):
        for j in range (0,A.shape[1],1):
            if A[i,j]==1:
                return(i)


def ultimalinha(A):
    for i in range(A.shape[0]-1,-1,-1):
        for j in range(A.shape[1]-1,-1,-1):
            if A[i,j]==1:
                return(i)

def primeiracoluna(A):
    for j in range(0,Ashape[1],1):
        for i in range(0,A.shape[0],1):
            if A[i,j]==1:
                return(j)


def ultimacoluna(A):
    for j in range(A.shape[1]-1,-1,-1):
        for i in range(A.shape[0]-1,-1,-1):
            if A[i,j]==1:
                return(j)
    

n=int(input('Numero de linhas: '))
m=int(input('Numero de colunas: '))
A=np.zeros((n,m))

for i in range (0, A.shape[0],1):
    for j in range(0,A.shape[1],1):
        A[i,j]=int(input('Digite o elemento da matriz:  '))

print(primeiralinha(A))
print(ultimalinha(A))
print(primeiracoluna(A))
print(ultimacoluna(A))

menorlinha=primeiralinha(A)
maiorlinha=ultimalinha(A)
menorcoluna=primeiracoluna(A)
maiorcoluna=ultimacoluna(A)


B=A[menorlinha:maiorlinha+1, menorcoluna:maiorcoluna+1]
print(B)






