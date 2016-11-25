# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def menorcoluna (lista):
    for j in range(0,lista.shape[1],1):
        for i in range(0,lista.shape[0],1):
            if lista[i,j]==1:
                mc=j
                break
    return mc

def maiorcoluna (lista):
    for j in range(0,lista.shape[1],1):
        for i in range(0,lista.shape[0],1):
            if lista[i,j]==1:
                md=j
    return md
    
def menorlinha (lista):
    for i in range(0,lista.shape[0],1):
        for j in range(0,lista.shape[1],1):
            if lista[i,j]==1:
                lc=i
                break
    return lc
    


def maiorlinha (lista):
    for i in range(0,lista.shape[0],1):
        for j in range(0,lista.shape[1],1):
            if lista[i,j]==1:
                ld=i
    return ld
    
linhas = input('digite numero de linhas:')
colunas = input('digite numero de colunas:')
a=np.zeros( (linhas,colunas) )

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('insira um elemento:')

menorcoluna (a) == menorcoluna_a
maiorcoluna (a) == maiorcoluna_a
menorlinha (a) == menorlinha_a
maiorlinha (a) == w

print (a[menorcoluna_a:y+1,z:w+1])