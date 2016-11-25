# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#DEFININDO A FUNÇÃO
def colunaEsquerda(a):
    ce=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i:(i+1)]:
            ce=i
            break
    return ce
def colunaDireita(a):
    ce=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i:(i+1)]:
            ce=i
            
    return ce

#COMECE AQUI ABAIXO

linhas=input('Digite a quantidade de linhas: ')
colunas=input('Digite a quantidade de colunas: ')

a=np.zeros((linhas,colunas))


for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz a: ')
        

print tranposta(a)