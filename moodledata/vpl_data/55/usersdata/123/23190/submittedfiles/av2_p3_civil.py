# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#DEFININDO FUNÇÃO PARA CÁLCULO DO PESO DA POSIÇÃO
def somatorio(f,l,c):
    somaL=0
    somaC=0
    for j in range (0,f.shape[1],1):
        if j!=c:
            somaL=somaL + f[l,j]
    for i in range (0,f.shape[0],1):
        if i!=l:
            somaC=somaC + f[i,c]
    soma = somaC+somaL
    return soma

#ENTRADA
d=input('Insira a dimensão da matriz:')
l=input('Insira o índice da linha:')
c=input('Insira o índice da coluna:')
f=np.zeros((d,d))
for i in range(0,f.shape[0],1):
    for j in range(0,f.shape[1],1):
        f[i,j]=input('Insira um elemento para a matriz:')

#SAÍDA
print somatorio(f,l,c)
