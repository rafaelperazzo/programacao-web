# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#Definindo a Função
def Peso(A,x,y):
    somaLinha=0
    for j in range(0,A.shape[1],1):
        if j!=y:
            somaLinha=somaLinha+A[x,j]
    somaColuna=0
    for i in range(0,A.shape[0],1):
        if i!=x:
            somaColuna=somaColuna+A[i,y]
            
    peso= somaLinha+somaColuna
#Entrada
n=input('Digite o valor da Dimensão da Matriz: ')
x=input('Digite o valor do indice X: ')
y=input('Digite o valor do indice Y: ')
A=np.zeros((n,n))
for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        A[i,j]=input('Digite um valor para a Matriz A: ')
        
#Saida        
print Peso(A,x,y)

