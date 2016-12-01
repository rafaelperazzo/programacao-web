# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def ColunaEsquerda(a):
    CE=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            CE=i
            break
    return CE

def ColunaDireita(a):
    CD=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            CD=i
            
    return CD

def linhaCima(a):
    LC=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            LC=i
            break
    return LC

def linhaBaixo(a):
    LB=0
   for i in range(0,a.shape[0],1):
       if 1 in a[i,:]:
           LB=i
           
    return LB

linhas=input('digite a quantidade de linhas:')
colunas=input('digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite um valor:')

print a[LC:LB+1,CE:CD+1]