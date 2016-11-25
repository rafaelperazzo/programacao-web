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
                if j>esquerda:
                    esquerda=j
def colunadireita(a):
    direita=0
    for i in range (0,a.shape[0],1):
        for j in range(0,shape[1],1):
            if a[i,j]==1:
                if j<direita:
                    direita=j
                
    return esquerda
def linhaesquerda(a):
    esquerda=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]==1:
                if i>esquerda:
                    esquerda=i
    return esquerda
def linhadireita(a):
    direita=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if [i,j]==1:
                if i<direita:
                    dirieta=i
    return direita
    
print a[colunaesquerda:colunadireita+1,linhadiesquerda:linhadireita+1]

