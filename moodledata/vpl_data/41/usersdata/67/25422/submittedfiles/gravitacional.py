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

lsl=[]
x=0
for i in range (0,a.shape[1],1):
        for j in range (0,a.shape[0],1):
            if i==x:
                soma = soma  + a[i,j]
                lsl.append=soma
        x=x+1


#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
