# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
a=[]
for r in range(0,n,1):
    soma_colunas= funcoes.a(A,r)
    a.append(soma_colunas)

o=[]
for l in range(0,n,1):
    soma_linhas= funcoes.o(A,l)
    o.append(soma_linhas)
    
soma_k=0
for k in range(0,n,1):
    soma_k=soma_k+(a[k]*(1/d[i,k]))

for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        T[i,j]=o[i]*((a[j]*(1/((d[i,j])**(alfa))))/soma_k)


#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
