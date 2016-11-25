# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def magica(x):
    cont=0
    
    #Soma das Linhas
    
    for i in range(0,x.shape[0]-1,1):
        a=sum(x[i,:])
        b=sum(x[i+1,:])
        if a==b:
            a=b
            b=0
            cont=cont+1
        else:
            break
        
    #Soma das colunas
    
    for i in range(0,x.shape[0]-1,1):    
        b=sum(x[:,i])
        if a==b:
            a=b
            b=0
            cont=cont+1
        else:
            break
    
    #Soma da Diagonal Principal
    somaDP=0
    for i in range(0,x.shape[0],1):
        somaDP=somaDP+x[i,i]
    if somaDP==a:
        cont=cont+1
        
    #Soma da Diagonal Secundária
    somaDS=0
    f=x.shape[0]-1
    for i in range(0,x.shape[0],1):
        somaDS=somaDS+x[i,f]
        f=f-1
    if somaDS==a:
        cont=cont+1
        
    return cont
        
#Criando a Matriz
dimensao=input('Digite a dimensão da matriz: ')
a=np.zeros((dimensao,dimensao))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz a: ')

print magica(a)

