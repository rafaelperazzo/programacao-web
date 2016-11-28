# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def SomaDiagonal1(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def SomaDiagonal2(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma
    
def SomaLinhas(a):
    s=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s

def SomaColunas(a):
    =[]
    for j in range (0,a.shape[0],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s
    
def quadradomagico(a):
    sd1=SomaDiagonal1(a)
    sd2=SomaDiagonal2(a)
    
    somaL=SomaLinhas(a)
    somac=SomaColunas(a)
    
    cont=0
    for i in range(0,len(somaL),1):
        if sd1==sd2==somaL[i]==somac[i]
        
    if cont==len(somaL):
        return True
    else:
        return False


n=input('Digite a dimensao da matriz quadrada:')
linhas=n
colunas=n
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite um elemento:')

