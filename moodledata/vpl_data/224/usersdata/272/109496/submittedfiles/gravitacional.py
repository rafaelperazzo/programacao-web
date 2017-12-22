# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = int(input('Digite a dimensao das matrizes: '))
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = int(input('Digite o valor de alfa: '))

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
a=[]
n=dimensao
for r in range(0,n,1):
    soma_colunas= funcoes.a(A,r)
    a.append(soma_colunas)

o=[]
for l in range(0,n,1):
    soma_linhas= funcoes.o(A,l)
    o.append(soma_linhas)
    

for i in range(0,T.shape[0],1):
    for j in range(0,T.shape[1],1):
        somatorio=0
        if (d[i,j]!=0):
            numerador=o[i]*a[j]*(1/((d[i,j])**alfa))
        for k in range(0,n,1):
            if (d[i,k]==0):
                T[i,j]=0
            elif (d[i,k]!=0):
                somatorio=somatorio+a[k]*(1/(d[i,k]))
        T[i,j]=numerador/somatorio
        


#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
