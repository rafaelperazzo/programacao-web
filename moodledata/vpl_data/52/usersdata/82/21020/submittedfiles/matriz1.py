# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def colunaEsquerda(a):
    
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            if a[i,j]==1:
                ce=j
                break
    return ce
               
def colunaDireita(a):
    
    for j in range (0,a.shape[1],1):
        for i in range (0, a.shape[0],1):
            if [i,j]==1:
                cd=j
    return cd
        
def linhaInferior(a):
    for i in range (0,a.shape[0],1):
        for j in range (0, a.shape[1],1):
            if [i,j]:
                if i==1:
                    li=i
                    break

def linhaSuperior(a):
    for i in range (0,a.shape[0],1):
        for j in range (0, a.shape[1],1):
            if [i,j]==1:
                ls=i
        
    colunas = colunaDireita-colunaEsquerda
    linhas = linhaSuperior-linhaInferior
    b = np.zeros ((linhas,colunas))
    for i in range (0,linhas,1):
        for j in range (0,colunas,1):
            b[i,j] = a[colunaEsquerda+j,linhasuperior+i]
    return b

linhas = input('Digite o numero de linhas:')
colunas = input ('Digite o numero de colunas:')
a = np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input ('Digite um elemento:')
print (a)
        
        
            



    