# -*- coding: utf-8 -*-
from __future__ import division

def a(A):
    a = []
    for j in range(0,n,1):
        somacoluna = 0
        for i in range(0,n,1):
            somacoluna = somacoluna + A[i,j]
        a.append(somacoluna)
    return a

def o(A):
    o = []
    for i in range(0,n,1):
        somalinha = 0
        for j in range(0,n,1):
            somalinha = somalinha + A[i,j]
        o.append(somalinha)
    return o

def T(a,o,d):
    a = a(A)
    o = o(A)
    T = np.zeros((n,n))
    for i in range(0,n,1):
        for j in range(0,n,1):
            somatorio = 0
            for k in range(0,n,1):
                if i!=k:
                    somatorio = somatorio + (a[k]*(1/d[i,k]))
                if i!=j:
                    T[i,j]= (o[i]*a[j]*(1/(d[i,j]))**alfa)/somatorio
    return T

def somaT(T):
    T = T(a,o,d)
    soma = 0
    for i in range(0,n,1):
        for j in range(0,n,1):
            soma = soma + T[i,j]
    return soma

