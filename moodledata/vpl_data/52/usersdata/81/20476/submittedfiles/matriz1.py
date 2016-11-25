# -*- coding: utf-8 -*-
from __future__ import division

def cesquerda(a):
    coluna=0
    for i in range(0,a.shape[1],1):
        for j in range(0,a.shape[0],1):
            if a[j,i]==1:
                coluna=i
                break
    return coluna
    
def cdireita(a):
    coluna=0
    i=a.shape[1]-1
    j=a.shape[0]-1
    while i>=0:
        while j>=0:
            if a[j,i]==1:
                coluna=1
                break
        j=j-1
    i=i-1
    return coluna
    
def lcima(a):
    linha=0
    for j in range(0,a.shape[0],1):
        for i in range(0,a.shape[1],1):
            if a[j,i]=1:
                linha=i
                break
    return linha
    
def lbaixo(a):
    linha=0
    i=a.shape[1]-1
    j=a.shape[0]-1
    while j>=0:
        while i>=0:
            if a[j,i]==1:
                linha==1
                break
        i=i-1
    j=j-1
    return linha
    
linhas=input('Digite a quantidade de linhas:')
colunas=input('Digite a quantidade de colunas:')
a=np.zeros((linhas,colunas))

for j in range(0,a.shape[0],1):
    for i in range(0,a.shape[1],1):
        a[j,i]=input('Digite um valor da matriz a:')
    