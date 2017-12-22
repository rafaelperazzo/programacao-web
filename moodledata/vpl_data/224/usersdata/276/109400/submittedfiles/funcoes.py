# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui

#funcaosomacolunas

def somacolunas (A):
    somacolunas = 0
    c = []
    for j in range (0, A.shape[0],1):
        somacolunas = 0
        for i in range (0,A.shape[0],1):
            somacolunas = somacolunas + A[i,j]
        c.append (somacolunas)
    return (c)

def somalinhas (A):
    somalinhas = 0
    d = []
    for i in range (0,A.shape[0],1):
        somalinhas = 0
        for j in range (0,A.shape[0],1):
            somalinhas = somalinhas + A[i,j]
        d.append (somalinhas)
    return (d)


        
    

