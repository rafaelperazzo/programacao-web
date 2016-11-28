# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunas(A):
    a=[]
    for j in range(0,A.shape[1],1):
        soma=0
        for i in range(0,A.shape[0],1):
            soma=soma+A[i,j]
        a.append(soma)
    return a
    
def somaLinhas(A):
    o=[]
    for i in range(0,A.shape[1],1):
        soma=0
        for j in range(0,A.shape[0],1):
            soma=soma+A[i,j]
        o.append(soma)
    return o

        
def matrizT(A,d,T,alfa):
    o=somaLinhas(A)
    a=somaColunas(A)
    for i in range(0,A.shape[0],1):
        for j in range(0,A.shape[1],1):
            if i!=j:
                soma = 0 
                for k in range(0,A.shape[0],1):
                    if k!=i:
                        soma = soma + a[k]/d[i,k]
                T[i,j]= o[i]*((a[j]/(d[i,j]**alfa))/(soma))
                T[i,j]=round(T[i,j],2)
    return T