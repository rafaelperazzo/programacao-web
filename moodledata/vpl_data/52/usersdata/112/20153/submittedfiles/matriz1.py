# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite o elemento:')
print a
def colunaesquerda(a):
    esquerda=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                if j>=esquerda:
                    esquerda=j
    return esquerda
def colunadireita(a):
    direita=0
    for i in range (0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                if j<=direita:
                    direita=j
                
    return direita
def linhaesquerda(a):
    esquerda=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                if i>=esquerda:
                    esquerda=i
    return esquerda
def linhadireita(a):
    direita=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if [i,j]==1:
                if i<=direita:
                    direita=i
    return direita
    
b=colunaesquerda(a)
c=colunadireita(a) + 1
d=linhaesquerda(a)
e=linhaesquerda(a) + 1
    
print a[b:c,d:e]

