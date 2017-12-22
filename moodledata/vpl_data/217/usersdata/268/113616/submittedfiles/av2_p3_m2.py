# -*- coding: utf-8 -*-
import numpy as np

dimensao=int(input('Digite a dimensão : '))
a= np.zeros((dimensao,dimensao))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o elemento: '))
        
def soma_linha(matriz,linha):
    soma=0
    for j in range(0,matriz.shape[1],1):
        soma= soma + matriz[linha,j]
    return(soma)
def soma_coluna(matriz,coluna):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma= soma + matriz[i,coluna]
    return(soma)
    
soma=0
soma_linhas=[]
for i in range(0,a.shape[0],1):
    soma= soma_linha(a,i)
    soma_linhas.append(soma)
    
soma=0
soma_colunas=[]
for j in range(0,a.shape[1],1):
    soma= soma_coluna(a,j)
    soma_coluna.append(soma)



    
    

