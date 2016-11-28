# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
linhas=input('Digite a quantidade de linhas:')
#colunas=input('Digite a quantidade de colunas:') A MATRIZ É QUADRADA, PORTANTO BASTA PEDIR UMA DIMENSÃO.
a=np.zeros((linhas,linhas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Digite o termo:')

def somaL(a):
    S=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        S.append(soma)
    return S

def somaC(a):
    S=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        S.append(soma)
    return S
    
def somadp(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def somads(a):
    soma=0
    i=0
    j=a.shape[1]-1
    while j>=0 and i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma

def quadradoM(a):
 
    SL=somaL(a)
    SC=somaC(a)
    SP=somadp(a)
    SS=somads(a)

    cont=0
    for i in range (0,len(somaL(a)),1):
        if SL[i]==SC[i]==SP==SS:
            cont=cont+1
    if cont==len(SL):
        return True
    else:
        return False
    
if quadradoM(a):
    print 'S'
else:
    print 'N'