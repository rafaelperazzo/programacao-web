# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

dimensao = input('Digite a dimensao das matrizes: ')
matrizT = input('Digite a Matriz T como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')

T = np.fromstring(matrizT, sep=' ').reshape(dimensao, dimensao)
D = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
print T
print D
