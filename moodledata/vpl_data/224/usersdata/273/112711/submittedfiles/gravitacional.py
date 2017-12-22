# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = int(input('Digite a dimensao das matrizes: '))
matrizA = input('Digite a Matriz A como uma única linha: ')
matrizD = input('Digite a Matriz D como uma única linha: ')
alfa = int(input('Digite o valor de alfa: '))

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
a=[]
soma=0
soma2=0
for j in range(0,A.shape[1],1):
    for i in range(0,A.shape[0],1):
        soma=soma+A[i,j]
    a.append(soma)
o=[]        
for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        soma2=soma2+A[i,j]
    o.append(soma2)
somatorio=0

for i in range(0,A.shape[0],1):
    for j in range(0,A.shape[1],1):
        for k in range(0,A.shape[1]-1,1):
            if d[i,j]!=0:
                somatorio=somatorio+(A[k]*1/(d[i,j]))
        if d[i,j]!=0:
            tj=0[1]*(a[j]*(1/(d[i,j]**alfa)))

    
        

#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
