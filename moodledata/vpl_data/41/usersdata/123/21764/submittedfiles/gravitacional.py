# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = input('Digite a Matriz A como uma única linha entre aspas: 0 10 15 12 13 0 23 14 31 43 0 11 19 32 18 0 ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: 0 3 2 4 4 0 5 6 3 6 0 3 3 5 4 0')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#PROCESSAMENTO
o= funcoes.somLinhas(A)
a= funcoes.somColunas(A)
T= funcoes.matriz(o,a,d,alfa,T)

#SAÍDA
somatorio = sum(sum(T))
print('%.4f' % somatorio)
