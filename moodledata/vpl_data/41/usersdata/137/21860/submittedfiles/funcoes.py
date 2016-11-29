# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunaA:
    b=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            b.append soma
            return b
def somaLinhaA:
    b=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape[1],1):
            soma=soma+a[i,j]
            b.append soma
            return b
def matrizT(o,a):
    o=somaLinhaA
    a=somaColunaA
    T=[]
    for i in range (0,d.shape[0],1):
        for j in range (0,d.shape[1],1):
            c[i,j]=o([i])*a([i])*i*((1/d[i,j]))*alfa
        soma=0
        for k in range (0,d.shape[1],1):
            soma[i,k]=soma+(a[k]*(1/d[i,k]))
            T[i,j]=c[i,j]/soma[i,k]
            
            
    