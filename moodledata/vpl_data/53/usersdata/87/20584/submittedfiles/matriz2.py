# -*- coding: utf-8 -*-
from __future__ import division

def somadiagonal1 (lista):
    soma=0
    for i in range(0,lista.shape[0],1):
        soma=soma+lista[i,i]
    return soma

def somadiagonal2 (lista):
    soma=0
    for i in range(0,lista.shape[0],1):
        soma=soma+lista[i,lista.shape[0]-i-1]
    return soma

def somadiagonal3 (lista):
    soma=0
    i=0
    j=lista.shape[0]
    while i<lista.shape[0]:
        soma=soma+lista[i,j]
        i=i+1
        j=j-1
    return soma

def somalinhas (lista):
    

