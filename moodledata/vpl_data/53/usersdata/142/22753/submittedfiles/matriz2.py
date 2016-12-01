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
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
    return soma

def SomaDasLinhas(a):
    s=[]
    for i in range(0,shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s

#ProgramaPrincipal:
linhas = input('Digite uma quantidade de linhas:')
colunas = input('Digite uma quantidade de colunas:')

x=np.zeros((linhas,colunas))

for i in range(0,x.shape[0],1):
    for j in range(0,x.shape[1],1):
        x[i,j]=input('Digite um valor:')

print SomaDiagonal1(x)

print SomaDiagonal2(x)