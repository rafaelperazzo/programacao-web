# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = input('Digite o valor de alfa: ')
n=dimensao
#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)




#comece aqui...
#INÍCIO
a=[]
for i in range(0,n,1):
    soma_l= soma_colunas (A,i)
    a.append(soma_l)
o=[]

for i in range(0,n,1):
  
#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
