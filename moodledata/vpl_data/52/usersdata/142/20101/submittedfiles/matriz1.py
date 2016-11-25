# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaesquerda(a):
    ce=0
    for i in range(0,a.shape[0],1):
        foi j in range(0,a.shape[1],1):
            if a[i,j]==1:
                ce=j
                break
    return ce

def colunadireita(a):
    cd=0
    for i in range(a.shape[0],1,1):
        foi j in range(0,a.shape[1],1):
            if a[i,j]==1:
                ce=j
                break
    return cd

def linhadecima(a):
    lc=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                lc=i
                break

def linhadebaixo(a):
    lb=0
    for j in range(a.shape[1],1,1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                lb=i
                break

#programa principal

linhas = input('Digite um valor de linhas:')
colunas = input('Digite um valor de colunas:')

a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um valor')

colunaesquerda(a)=colunaesquerda
colunadireita(a)=colunadireita
linhadecima(a)=linhadecima
linhadebaixo(a)=linhadebaixo

recorte=c[linhadecima:(linhadebaixo+1),colunaesquerda:(colunadireita+1)]

print recorte