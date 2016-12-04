# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunaA(A):
    s=[]
    for j in range (0,A.shape[1],1):
        soma=0
        s[j]=soma+A[:,j]
    return s
        
def somaLinhaA(A):
    s=[]
    for i in range (0,A.shape[0],1):
        soma=0
        s[i]=soma+A[i,:]
    return s
    
def matriz(a,o,d):
    sc=somaColunaA(A)
    sl=somaLinhaA(A)
    T=np.zeros((len(a),len(a)))
    for i in range (0,d.shape[0],1):
        for j in range (0,d.shape[1],1):
            soma=0
            for k in range (0,d.shape[0],1):
                if i!=k:
                    soma=soma+a[k]*(1/d[i,k])
                if i!=j:
                    c[i,j]=(o[i]*a[j]*(1/(d[i,j]))**alfa)/soma
    return T
            

    