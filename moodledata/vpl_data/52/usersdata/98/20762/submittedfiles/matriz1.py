# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#DEFININDO A FUNÇÃO
def colunaEsquerda(a):
    ce=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            ce=i
            break
    return ce
    
def colunaDireita(a):
    cd=0
    for i in range(0,a.shape[1],1):
        if 1 in a[:,i]:
            cd=i
    return cd
    
def linhaSuperior(a):
    ls=0
    for i in range(0,a.shape[1],1):
        if 1 in a[i,:]:
            ls=i
            break
    return ls
    
def linhaInferior(a):
    li=0
    for i in range(0,a.shape[1],1):
        if 1 in a[i,:]:
            li=i
    return li
    
def recorte(a):
    e=linhaSuperior(a)
    f=(linhaInferior(a))+1
    g=colunaEsquerda(a)
    h=(colunaDireita(a))+1
    
    b=a[e:f,g:h]
    
    return b
    
#DEFININDO A MATRIZ

linhas=input('Digite a quantidade de linhas: ')
colunas=input('Digite a quantidade de colunas: ')

a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para a matriz a: ')
        
print(recorte(a))

