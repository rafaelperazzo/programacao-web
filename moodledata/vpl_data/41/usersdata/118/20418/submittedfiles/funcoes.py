# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somatorioColunas(A):
    a = []
    for i in range(0,A.shape[1],1):
        a.append(sum(A[:,i]))
    return a

def somatorioLinhas(A):
    o = []
    for i in range(0,A.shape[1],1):
        o.append(sum(A[i,:]))
    return o

def MatrizT(a,o,d,alfa):
    linhas = d.shape[0]
    colunas = d.shape[1]
    T = np.zeros((linhas,colunas))
    
    for i in range(0,d.shape[0],1):
        for j in range(0,d.shape[1],1):
            soma = 0
            for k in range(0,d.shape[1],1):
                soma = soma + a[k]*(1/d[i,k])
                
            T[i,j] = o[i]* ((a[j]*(1/(d[i,j]**alfa)))/soma)
    return T
                
                
                
                
                
