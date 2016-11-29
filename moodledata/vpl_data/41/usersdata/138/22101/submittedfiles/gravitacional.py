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
def somaC(m):
    b=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],):
            soma=soma+a[i,j]
        b.append(soma)
    return b

def somaL(m):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma= soma+a[i,j]
        b.append(soma)
    return b
    
def matrizT(a,o,d):
    sc=somaC(m)
    sl=somaL(m)
    T=[]
    for i in range(0,d.shape[0],1):
        for j in range(0,d.shape[1],1):
            Tc[i,j]=(sc[i])*(sl[i])*((1/d[i,j]))**alfa
        soma=0
        for k in range(0,dimensao,1):
            soma[i,k]=soma+(sc[k]*(1/d[i,k]))
        T[i,j]=Tc[i,j]/soma[i,k]
        T.append(T[i,j])
    return T
  
#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)





























