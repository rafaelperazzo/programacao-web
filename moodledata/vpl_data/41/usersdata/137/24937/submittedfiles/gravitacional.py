# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = raw_input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = raw_input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
def somaColunaA(A):
    b=[]
    for j in range (0,A.shape[1],1):
        b.append(sum(A[:,j]))
    return b
        
def somaLinhaA(A):
    b=[]
    for i in range (0,A.shape[0],1):
        b.append(sum(A[i,:]))
    return b
    
def matriz(a,o,d):
    sc=somaColunaA(A)
    sl=somaLinhaA(A)
    T=np.zeros((len(a),len(a)))
    for i in range (0,d.shape[0],1):
        for j in range (0,d.shape[1],1):
            soma=0
            for k in range (0,d.shape[0],1):
                if i!=k:
                    soma=soma+a[k]*(1/d[i,k])
                if i!=j:
                    c[i,j]=(o[i]*a[j]*(1/(d[i,j]))**alfa)/soma
    return T
'''o=funcoes.somaLinhaA(A)
a=funcoes.somaColunaA(A)
T=funcoes.matriz(a,o,d)'''


#SAÍDA
o=somaLinhaA(A)
a=somaColunaA(A)
T=matriz(a,o,d)

somatorio = sum(sum(T))
print('%.4f' % somatorio)
