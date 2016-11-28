# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menorColuna(a):
    for j in range (0, a.shape[1], 1):
        for i in range (0, a.shape[0], 1):
            if a[i,j] == 1:
                return j
def maiorColuna(a):
    for j in range (0, a.shape[1], 1):
        for i in range (0, a.shape[0], 1):
            if a[i,j] == 1:
                CD = j
    return CD
def menorLinha(a):
    for i in range (0, a.shape[0], 1):
        for j in range (0, a.shape[1], 1):
            if a[i,j] == 1:
                return i
def maiorLinha(a):
    for i in range (0, a.shape[0], 1):
        for j in range (0, a.shape[1], 1):
            if a[i,j] == 1:
                LB = i
    return LB

linhas = input('Digite a quantidade de linhas:')
colunas = input('Digite a quantidade de colunas:')
a = np.zeros( (linhas,colunas) )

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite um elemento para a:')

print ( a[menorLinha(a):LB+1,menorColuna(a):CD+1] )