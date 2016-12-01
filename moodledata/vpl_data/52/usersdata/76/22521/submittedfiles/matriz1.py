# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menorColuna(a):
    for j in range(0,a.shape(1),1):
        for i in range(0,a.shape(0),1):
            if a[i,j] == 1:
                return j

def maiorColuna(a):
    for j in range(0,a.shape(1),1):
        for i in range(0,a.shape(0),1):
            if a[i,j] == 1:
                CD = j
    return CD
    
def menorLinha(a):
    for i in range(0,a.shape(0),1):
        for j in range(0,a.shape(1),1):
            if a[i,j] == 1:
                return i

def maiorLinha(a):
    for i in range(0,a.shape(0),1):
        for j in range(0,a.shape(1),1):
            if a[i,j] == 1:
                LB = i
    return LB

L = input('Digite o numero de linhas:')
C = input('Digite o numero de colunas:')
a = np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite os elementos:')
    
print(LC:LB+1,CE:CD+1)