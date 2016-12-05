# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import funcoes

def soma_coluna(A, dimensao):
    a = []
    for i in range(0, dimensao, 1):
        s = 0
        for j in range(0, dimensao, 1):
            s = s + A[j,i]
        a.append(s)
        
def soma_linha(A, dimensao):
    o = []
    for i in range(0, dimensao, 1):
        s = 0
        for j in range(0, dimensao, 1):
            s = s + A[i,j]
        o.append(s)

def soma(a,d,i):
    s = 0
    for j in range(0, len(a), 1):
        s = s + (a[i])*(d[i,j])
    return s

                #c é o coeficiente
 

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
a = soma_coluna(matrizA, dimensao)
o = soma_linha(matrizA, dimensao)
print (a)
print (o)

for i in range(0, T.shape[0], 1):
        for j in range(0, T.shape[0], 1):
            T[i,j] = ((o[i])*(a[j]))/((d[i,j]**alfa)*(soma(a,d,i)))
print T[0:(dimensao + 1), 0:(dimensao + 1)]
#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
