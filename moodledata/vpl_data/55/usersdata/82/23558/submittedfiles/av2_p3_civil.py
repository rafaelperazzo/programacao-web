# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas = input('Digite a quantidade de linhas:')
colunas = input('Digite a quantiudade de colunas:')
a = np.zeros ((linhas,colunas))

def somaL(a):
    soma=0
    for i in range (0,a.shape[0],1):
        a.append(input('Digite um elemento:'))
        soma=soma+a[i]
    return soma

def somaC(a):
    for j in range (0,a.shape[1],1):
        a.append(input('Digite um elemento:'))
        soma = soma+a[j]
    return soma
        
def peso(a):
    peso = somaL + somaC
    for i in range(0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[i,j]
        
        