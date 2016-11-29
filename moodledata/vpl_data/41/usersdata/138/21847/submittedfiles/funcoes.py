# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

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
    
def matrizT(a,o):
    a=somaC(m)
    o=somaL(m)
    for i in range(0,d.shape[0],1):
        for j in range(0,d.shape[1],1):
            Tc[i,j]=(o[i])*(a[i])*((1/d[i,j]))**alfa
        soma=0
        for k in range(0,d.shape[1],1):
            soma[i,k]=soma+(a[k]*(1/d[i,k]))
        T[i,j]=Tc[i,j]/soma[i,k]
        T.append(T[i,j])

        
c=matrizT(a,o)
print c
            
    
    
    
    
    
    
    
    
    
            
