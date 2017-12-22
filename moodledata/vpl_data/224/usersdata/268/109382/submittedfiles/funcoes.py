# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def soma_linhas (b,l):
    soma=0
    for j in range(0,b.shape[1],1):
        soma= soma + b[l,j]
    return(soma)
def soma_colunas (b,c):
    soma=0
    for i in range (0,b.shape[0],1):
        soma= soma + b[i,c]
    return(soma)