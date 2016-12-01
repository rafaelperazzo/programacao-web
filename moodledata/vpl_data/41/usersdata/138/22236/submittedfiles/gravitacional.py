# -*- coding: utf-8 -*-
from __future__ import division
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
def somaC(A):
    b=[]
    for j in range(0,A.shape[1],1):
        soma=0
        for i in range(0,A.shape[0],1):
            soma=soma+A[i,j]
        b.append(soma)
    return b

def somaL(A):
    b=[]
    for i in range(0,A.shape[0],1):
        soma=0
        for j in range(0,A.shape[1],1):
            soma= soma+A[i,j]
        b.append(soma)
    return b
    
def matrizT(a,o,d):
    sc=somaC(A)
    sl=somaL(A)
    T=np.zeros( (len(a),len(a)) )
    for i in range(0,d.shape[0],1):
        for j in range(0,d.shape[1],1):
            soma=0
            for k in range(0,d.shape[0],1):
                if i!=k:
                    soma = soma + a[k]*(1/d[i,k]) #Continue aqui... i tem q ser diferente de k
                if i!=j:
                    T[i,j]= (o[i]*a[j]*(1/(d[i,j]))**alfa)/soma #i diferente de j
        
    return T
  
#SAÍDA
a = somaC(A)
o = somaL(A)
T = matrizT(a,o,d)
somatorio = sum(sum(T))
print('%.4f' % somatorio)





























