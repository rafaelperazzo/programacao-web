# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#Função:
def SomaDiagonal1(a):
    somatorio=0
    for i in range(0,a.shape[0],1):
        somatorio = somatorio + a[i,i]
    return somatorio

def SomaDiagonal2(a):
    somatorio=a[0,a.shape[0]]
    for i in range(0,a.shape[0],1):
        for j in range(a.shape[1],1,1):
            somatorio = somatorio + a[i+1,j-1]
    return somatorio

#ProgramaPrincipal:
linhas = input('Digite uma quantidade de linhas:')
colunas = input('Digite uma quantidade de colunas:')

x=np.zeros((linhas,colunas))

for i in range(0,x.shape[0],1):
    for j in range(0,x.shape[1],1):
        x[i,j]=input('Digite um valor:')

print SomaDiagonal1(x)

print SomaDiagonal2(x)