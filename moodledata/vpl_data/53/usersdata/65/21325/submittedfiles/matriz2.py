# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#FUNÇÕES
#diagonal_principal

def Dprincipal(x):
    soma=0
    for i in range(0,x.shape[0],1):
        soma=soma+x[i,j]
    return soma

#diagonal_secundaria
def Dsecundaria(x):
    soma=0
    i=0
    j=x.shape[0]-1
    while i<(x.shape[0]):
        soma=soma+x[i,j]
        i=i+1
        j=j-1
    return soma
    
#linhas
def SomaLinhas(x):
    s=[]
    for i in range(0,x.shape[0],1):
        soma=0
        for j in range(0,x.shape[1],1):
            soma=soma+x[i,j]
        s.append(soma)
    return s

#colunas
def SomaColunas(x):
    s=[]
    for j in range(0,x.shape[1],1):
        soma=0
        for i in range(0,x.shape[0],1):
            soma=soma+x[i,j]
        s.append(soma)
    return s
    
#quadrado_magico
def Qmagico(x):
    dp=Dprincipal(x)
    ds=Dsecundaria(x)
    sl=SomaLinhas(x)
    sc=SomaColunas(x)
    
    contador=0
    for i in range(0,len(sl),1):
        if dp==ds==sl[i]==sc[i]:
            contador=contador+1
    
    if contador==len(sl):
        return True
    else:
        return False

#PRINCIPAL
dim=input('Digite a dimensão da matriz quadrada : ')

matriz=np.zeros((dim,dim))

for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=input('Digite os elementos da matriz: ')

if Qmagico(matriz):
    print('S')
else:
    print('N')
    