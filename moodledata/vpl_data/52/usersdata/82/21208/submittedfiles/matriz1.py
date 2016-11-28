# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaEsquerda(a):
    ce=0
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                ce=j
    return ce
               
def colunaDireita(a):
    cd=0
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if [i,j]==1:
                cd=j
    return cd
        
def linhaBaixo(a):
    lb=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if [i,j]==1:
                lb=i
    return lb

def linhaCima(a):
    lc=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if [i,j]==1:
                lc=i
    return lc
        
lb=linhaBaixo
lc=linhaCima
cd=colunaDireita
ce=colunaEsquerda

linhas = input ('Digite a quantidade de linhas:')
colunas = input ('Digite a quantidade de colunas:')

a = np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('Digite um elemento:')

print a[lc:lb+1,ce:cd+1]
        
            



    