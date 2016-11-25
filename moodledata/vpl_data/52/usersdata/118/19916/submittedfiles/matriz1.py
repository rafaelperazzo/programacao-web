# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaEsquerda(a):
    ce = 0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            ce = i
            break
    return ce
    
def colunaDireita(a):
    cd = 0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            ce = i
    return ce

def linhaEsquerda(a):
    le = 0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            le = i
            break
    return le
    
def linhaDireita(a):
    ld = 0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            le = i
    return le    

linhas = input('Digite a quantidade de linhas:')
colunas = input('Digite a quantidade de colunas:')

a = np.zeros ((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = input('Digite um valor binário:')

ce = colunaEsquerda(a)
cd = colunaDireita(a)
le = linhaEsquerda(a)
ld = linhaDireita(a)

print(a[ce:cd+1 , le:ld+1])

    
    