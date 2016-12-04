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
A = np.fromstring(matrizA, sep='5 ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' 5').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
print A
print D


#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
