# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somacoluna (A) :
    a = []
    soma = 0
    for j in range (0,A.shaped[1],1) :
        soma = 0
        for i in range (0,A.shaped[0],1) :
            soma = soma + A[i,j]
        a.append (soma)
    return(a)
def somalinha (A) :
    o = []
    soma = 0
    for i in range (0,A.shaped[0],1) :
        soma = 0
        for j in range (0,A.shaped[1],1) :
            soma = soma + A[i,j]
        o.append (soma)
    return (o)
