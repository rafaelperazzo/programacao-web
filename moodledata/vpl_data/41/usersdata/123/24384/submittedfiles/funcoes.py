# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#DEFININDO FUNÇÃO PARA SOMATÓRIO DAS COLUNAS DE UMA MATRIZ
def somColunas(a):
    b=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma +a[i,j]
        b.append(soma)
    return b    
        
#DEFININDO FUNÇÃO PARA SOMATÓRIO DA LINHAS DE UMA MATRIZ
def somLinhas(a):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma +a[i,j]
        b.append(soma)
    return b 

#DEFININDO FUNÇÃO PARA CÁLCULO DA MATRIZ T
def matriz(o,a,d,alpha,t):
    for i in range(0,t.shape[0],1):
        for j in range(0,t.shape[1],1):
            soma = 0 
            for k in range(0,t.shape[0],1):
                if i!=k:
                    soma = soma + (a[k]/d[i,k]) 
            if i!=j:
                t[i,j]= o[i]*((a[j] * (1/(d[i,j]**alpha)))/soma) 
            else:
                t[i,j]=0
    return t
