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

def MatrizInversaElevadaAlfa(b,a):
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
            b[i,j] = ((b[i,j]**a)**-1)
    return b

def MatrizInversa(b):
    for i in range(0,b.shape[0],1):
        for j in range(0,b.shape[1],1):
            b[i,j] = (b[i,j]**-1)
    return b

def ListaVezesMatriz(a,b):
    c = []
    for j in range(0,len(a),1):
        soma = 0
        for i in range(0,b.shape[1],1):
            soma = soma + (a[i]*b[i,j])
        c.append(soma)
    return c
