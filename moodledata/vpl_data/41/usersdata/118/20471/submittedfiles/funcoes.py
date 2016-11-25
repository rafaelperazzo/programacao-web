# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#escreva suas funcoes aqui
def somatorioColunas(b):
    a = []
    for i in range(0,b.shape[1],1):
        a.append(sum(b[:,i]))
    return a

def somatorioLinhas(b):
    o = []
    for i in range(0,b.shape[1],1):
        o.append(sum(b[i,:]))
    return o

def MatrizT(a,o,d,alfa):
    linhas = d.shape[0]
    colunas = d.shape[1]
    T = np.zeros((linhas,colunas))
    
    for i in range(0,d.shape[0],1):
        for j in range(0,d.shape[1],1):
            soma = 0
            for k in range(0,d.shape[1],1):
                
                if d[i,k] != 0:
                    soma = soma + a[k]*(1/d[i,k])
                
                
            if (d[i,j]**alfa) != 0:
                T[i,j] = o[i]* ((a[j]*(1/(d[i,j]**alfa)))/soma)
    return T
                
                
                
                
                
