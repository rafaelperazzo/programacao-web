# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = input('Digite a Matriz T como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#INÍCIO
a = funcoes.somatorioColunas(matrizA)
o = funcoes.somatorioLinhas(matrizA)
T = funcoes.MatrizT(a,o,matrizD,alfa)

#SAÍDA
print T
somatorio = sum(sum(T))
print('%.4f' % somatorio)
