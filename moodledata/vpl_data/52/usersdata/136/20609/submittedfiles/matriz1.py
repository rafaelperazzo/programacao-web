# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menorColuna(a):
    for j in range (0, a.shape[1], 1):
        for i in range (0, a.shape[0], 1):
            if a[i,j] == 1:
                CE = j
                break
    return CE
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
                LC = i
                break
    return LC
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
menorColuna(a) = CEE
maiorColuna(a) = CDD
menorLinha(a) = LCC
maiorLinha(a) = LBB
print ( a[LCC:LBB+1,CEE:CDD+1] )