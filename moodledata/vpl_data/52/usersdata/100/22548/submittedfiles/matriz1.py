# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
""" 
EXERCÍCIO 42
RECORTE RETANGULAR:

0 0 0 0 0 
0 1 0 0 0
1 0 0 0 1
0 0 0 0 0
0 0 0 0 0

> coluna da esquerda 
> coluna da direita 
> linha de cima
> linha de baixo

"""
linhas = input('Numero de linhas:')
colunas = input('Numero de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('elementos:')
def colunaEsquerda(a):
    ce = 0
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i:(i+1)]:
            ce = i
            break
    return ce
def colunaDireita(a):
    cd = 0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i:(i+1)]:
            cd=i
    return cd
    
def primeira_linha(a):
    pL = 0
    for i in range(0,a,shape[0],1):
        if 1 in a[i,:]:
            pL = i
            break 
    return pL
def ultima_linha(a):
    uL = 0
    for i in range(0,a,shape[0],1):
        if 1 in a[i,:]:
            uL = i
    return uL
print a[primeira_linha(a):(ultima_linha(a)+1),colunaEsquerda(a):(colunaDireita(a)+1)]