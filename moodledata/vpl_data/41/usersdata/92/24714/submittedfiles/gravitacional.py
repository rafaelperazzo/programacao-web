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


def funcaoT(matrizA,matrizD,alpha,a,o):
    T= np.zeros((matrizA.shape(0),matrizA.shape(1)))
    for i in range(0, matrizA.shape(0),1):
        for j in range(0, matrizA.shape(1),1):
            soma=0
            for k in range(0, matrizA.shape(1),1):
                soma= soma+ a[k]*(1/matrizD[i,k])
            matrizT[i,j]= o[i]*(a[j]*(1/(matrizD[i,j]**alpha))/soma)
    return T
 
    
o1=[]
for i in range(0, matrizA.shape(0),1):
    soma=0
    for j in range(0, matrizA.shape(1),1):
        soma= soma+ matrizA[i,j]
    o1.append(soma)
o=[]
for i in range(0, matrizA.shape(0),1):
    o.append(o1[matrizA.shape(0)-1-i)


a1=[]
for j in range(0, matrizA.shape(1),1):
    soma=0
    for i in range(0, matrizA.shape(0),1):
        soma= soma+ matrizA[i,j]
    a1.append(soma)
a=[]
for i in range(0, matrizA.shape(0),1):
    a.append(a1[matrizA.shape(0)-1-i)
   

T= funcaoT(matrizA,matrizD,alpha,a,o)

somatorio = sum(sum(T))
print('%.4f' % somatorio)
