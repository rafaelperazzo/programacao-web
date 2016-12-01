# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunaA(A):
    b=[]
    for j in range (0,A.shape[1],1):
        soma=0
        for i in range(0,A.shape[0],1):
            soma=soma+A[i,j]
            b.append (soma)
            return b
def somaLinhaA(A):
    b=[]
    for i in range (0,A.shape[0],1):
        soma=0
        for i in range(0,A.shape[1],1):
            soma=soma+A[i,j]
            b.append (soma)
            return b

def matriz(T,d,c,o,a):
    T=np.zeros((len(a),len(a)))
    for i in range (0,d.shape[0],1):
        for j in range (0,d.shape[1],1):
            c[i,j]=(o[i]*a[j]*(1/(d[i,j]))**alfa)/soma
                
    return T
            

    