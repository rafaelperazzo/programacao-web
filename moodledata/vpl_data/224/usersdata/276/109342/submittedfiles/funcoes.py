# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui

#funcaosomacolunas

def somacolunas (A):
    somacolunas = 0
    a = []
    for j in range (0, dimensao,1):
        somacolunas = 0
        for i in range (0,dimensao,1):
            somacolunas = somacolunas + A[i,j]
        a.append (somacolunas)
    return (a)

def somalinhas (A):
    somalinhas = 0
    o = []
    for i in range (0,dimensao,1):
        somalinhas = 0
        for j in range (0,dimensao,1):
            somalinhas = somalinhas + A[i,j]
        o.append (somalinhas)
    return (o)


        
    

