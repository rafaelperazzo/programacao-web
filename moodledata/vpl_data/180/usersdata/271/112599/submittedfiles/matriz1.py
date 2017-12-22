# -*- coding: utf-8 -*-
import numpy as np
#FUNÇÕES
def primeiralinha (A) :
    for i in range (0,A.shape[0],1) :
        for j in range (0,A.shape[1],1) :
            if A[i,j] == 1 :
                return(i)
            
def primeiracoluna (A) :
    for j in range (0,A.shape[1],1) :
        for i in range (0,A.shape[0],1) :
            if A[i,j] == 1 :
                return(j)
            
def ultimalinha (A) :
    for i in range (A.shape[0],-1,-1) :
        for j in range (0,A.shape[1],1) :
            if (A[i,j]==1) :
                return(i)

def ultimacoluna(A) :
    for j in range (A.shape[1],-1,-1) :
        for i in range (0,A.shape[0],1) :
            if A[i,j] == 1 :
                return (j)
                
#ENTRADA
n = int(input('Digite a quantidade de linhas : '))
m = int(input('Digite a quantidade de colunas : '))
a = np.zeros((n,m))
#PROCESSAMENTO
for i in range (0,n,1) :
    for j in range (0,m,1) :
        a[i,j] = int(input('Digite o elemento : '))
menorlinha = primeiralinha(a)
maiorlinha = ultimalinha(a)
menorcoluna = primeiracoluna(a)
maiorcoluna = ultimacoluna(a)
#SAIDA
b = a[menorlinha:maiorlinha+1,menorcoluna:maiorcoluna+1]
print(b)
        
                
        

