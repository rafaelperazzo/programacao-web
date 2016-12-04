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

def somacolunas(matriz):
    a=[]
    for j in range (0,matriz.shape[0],1):
        cont=0
        for i in range (0,matriz.shape[1],1):
            cont=cont+matriz[i,j]
        
        a.append(cont)
    
    return a



def somalinhas(matriz):
    a=[]
    for i in range (0,matriz.shape[1],1):
        cont=0
        for j in range (0,matriz.shape[0],1):
            cont=cont+matriz[i,j]
        
        a.append(cont)
    
    return a
    
def sum(T):
    cont=0
    for i in range (0,T.shape[0],1):
        for j in range(0,T.shape[1],1):
            cont=cont+T[i,j]
    
    return cont
    
    
a=somacolunas(A)
o=somalinhas(A)

for i in range (0,len(a),1):
    cont=0
    for k in range (0,len(a),1):
        cont=cont+(a[k]*(1/d[i,k]))
    for j in range (0,len(a),1):
        T[i,j]=o[i]*(a[j]*(1/(d[i,j]**alfa))/cont)
        
        

#SAÍDA

somatorio = sum(T)
print('%.4f' % somatorio)