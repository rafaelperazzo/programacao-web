# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaEsquerda(a):
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i]:
            c1=i
            break
    return c1

def colunaDireita(a):
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i]:
            c2=i
    return c2

def linhaAcima(a):
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
            l1=i
            break
    return l1

def linhAbaixo(a):
    for i in range (0,a.shape[0],1):
        if 1 in a[i,:]:
            l2=i
    return l2

linhas=input('Quantidade de linhas: ')
colunas=input('Quantidade de colunas: ')

a=np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um termo: ')

print a[linhaAcima(a):linhaAbaixo(a)+1,colunaEsquerda(a):colunaDireita(a)+1]