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

def MatrizT(a,o,d):
    for i in range(0,d.shape[0],1):
        
