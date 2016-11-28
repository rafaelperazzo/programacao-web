# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = raw_input('Digite a Matriz T como uma única linha: ')
matrizD = raw_input('Digite a Matriz D como uma única linha: ')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
T = funcoes.gravitacional(A,d,alfa)

#SAÍDA
#print T
somatorio = sum(sum(T))
print('%.4f' % somatorio)
#print('241.9032')
