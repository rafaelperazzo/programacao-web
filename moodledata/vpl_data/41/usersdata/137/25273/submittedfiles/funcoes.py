# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunaA(A):
    b=[]
    for j in range (0,A.shape[1],1):
        b.append(sum(A[:,j]))
    return b
 
def somaLinhaA(A):
    b=[]
    for i in range (0,A.shape[0],1):
        b.append(sum(A[i,:]))
    return b
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
                T[i,j]=(o[i]*a[j]*(1/(d[i,j]))**alfa)/soma
    return T
            

    