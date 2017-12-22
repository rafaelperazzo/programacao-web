# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui

def o(A,n):
    soma=0
    o=[]
        for j in range (0,A.shape[1],1):
            soma=soma+A[n,j]
        o.append(soma)
    return (o)

def A(A,n):
    soma=0
    a=[]
        for i in range (0,A.shape[0],1):
            soma=soma+A[i,n]
        a.append(soma)
    return (o)


