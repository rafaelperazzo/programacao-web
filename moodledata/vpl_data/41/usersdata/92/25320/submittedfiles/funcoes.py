# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui

def funcaoT(A,d,alfa,a,o):
    T= np.zeros((A.shape[0],A.shape[1]))
    for i in range(0, A.shape[0],1):
        for j in range(0, A.shape[1],1):
            soma=0
            for k in range(0, A.shape[1],1):
                if d[i,k]!=0:
                    soma= soma+ a[k]*(1/d[i,k])
            if d[i,j]!=0:
                T[i,j]= o[i]*(a[j]*((1/(d[i,j]**alfa))/soma))
    return T
    
def somalinhas(A):    
    o1=[]
    for i in range(0, A.shape(0),1):
        soma=0
        for j in range(0, A.shape(1),1):
            soma= soma+ A[i,j]
        o1.append(soma)
    o=[]
    for i in range(0, A.shape(0),1):
        o.append(o1[dimensao-1-i])
    return o

def somacolunas(A):
    a1=[]
    for j in range(0, A.shape(1),1):
        soma=0
        for i in range(0, A.shape(0),1):
            soma= soma+ A[i,j]
        a1.append(soma)
    a=[]
    for i in range(0, A.shape(1),1):
        a.append(a1[dimensao-1-i])
    return a
