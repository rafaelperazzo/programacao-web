# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):

def somadp(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
def somads(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma= soma+a[i,a.shape[0]-1-i,1]
    return soma
def somal(a):
    S=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        S.append(soma)
    return S
print somaL(a)            
def quadradomagico(a):
    if somal(a)==somadp(a)==somads(a):
        return 'Sim'
    else:
        return 'Não'
print quadradomagico(a)            