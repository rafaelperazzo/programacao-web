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
        
def linhaBaixo(a):
    for i in range (0,a.shape[0],1):
        for j in range (0, a.shape[1],1):
            if [i,j]==1:
                li=i
                break
    return li

def linhaCima(a):
    for i in range (0,a.shape[0],1):
        for j in range (0, a.shape[1],1):
            if [i,j]==1:
                ls=i
    return ls
        
lb=linhaBaixo
lc=linhaCima
ld=linhaDireita
le=linhaEsquerda

linhas = input ('Digite a quantidade de linhas:')
colunas = input ('Digite a quantidade de colunas:')

b = np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input('Digite um elemento:')):

print (a[lc:lb+1, ce:cd+1])
        
            



    