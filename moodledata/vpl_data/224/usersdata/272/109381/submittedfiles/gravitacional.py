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
for i in range(0,n,1):
    soma_colunas= funcoes.a(A,i)
    a.append(soma_colunas)

o=[]
for j in range(0,n,1):
    soma_linhas= funcoes.o(A,j)
    o.append(soma_linhas)
    
for i in range 



#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
