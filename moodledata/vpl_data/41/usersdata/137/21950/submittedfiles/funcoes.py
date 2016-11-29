# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunaA(m):
    b=[]
    for j in range (0,m.shape[1],1):
        soma=0
        for i in range(0,m.shape[0],1):
            soma=soma+m[i,j]
            b.append (soma)
            return b
def somaLinhaA(m):
    b=[]
    for i in range (0,m.shape[0],1):
        soma=0
        for i in range(0,m.shape[1],1):
            soma=soma+m[i,j]
            b.append (soma)
            return b

def matriz(T,d,c,o,a):
    for i in range (0,c.shape[0],1):
        for j in range (0,c.shape[1],1):
            c[i,j]=o([i])*a([i])*i*((1/d[i,j]))*alfa
                return c
            

    