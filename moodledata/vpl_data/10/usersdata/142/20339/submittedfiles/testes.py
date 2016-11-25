# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#FUNÇÃO DE TESTE
def linhadecima(a):
    lc=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                lc=i
                break
    return lc

def linhadebaixo(a):
    lb=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                lb=i
    return lb

def colunaesquerda(a):
    ce=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                ce=j
                break
    return ce

def colunadireita(a):
    cd=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                cd=j
                break
    return cd
#PROGRAMA PRINCIPAL
linhas=input('Digite uma quantidade de linhas:')
colunas=input('Digite uma quantidade de colunas:')

a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')

print a[:,:]

print a[0:2,0:2]

print linhadecima(a)

print linhadebaixo(a)

print colunaesquerda(a)

print colunadireita(a)