# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = int(input('Digite a dimensao das matrizes: '))
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = int(input('Digite o valor de alfa: '))
n=dimensao

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)





#INÍCIO
a=[]
for i in range(0,n,1):
    soma_c= funcoes.soma_colunas(A,i)
    a.append(soma_c)
o=[]
for i in range(0,n,1):
    soma_l= funcoes.soma_linhas(A,i)
    o.append(soma_l)
    
for i in range(0,T.shape[0],1):
    somatorio=0
    for j in range(0,T.shape[1],1):
        
        numerador= o[i]*a[j]*(1/((d[i,j])**alfa))
        for k in range(0,n,1):
            somatorio= somatorio + a[k]*(1/(d[i,k]))
        T[i,j]=(numerador)/(somatorio)
    
  
#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
