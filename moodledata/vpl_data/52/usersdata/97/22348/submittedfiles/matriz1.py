# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def ColunaEsquerda(a):
    CE=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                CE=j
                break
        return CE

def ColunaDireita(a):
    CD=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while j>=0:
        while i>=0:
            if a[i,j]==1:
                CD=j
            i=i-1
        j=j-1
    return CD

def linhaCima(a):
    LC=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                LC=j
                break
        return LC

def linhaBaixo(a):
    LB=0
    j=a.shape[1]-1
    i=a.shape[0]-1
    while i>=0:
        while j>=0:
            if a[i,j]==1:
                LB=i
                break
            j=j-1
        i=i-1
    return LB

linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um valor:')

print a[LC:LB+1,CE:CD+1]