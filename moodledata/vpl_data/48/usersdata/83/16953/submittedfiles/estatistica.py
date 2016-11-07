# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviop(lista) :
    soma = 0
    for i in range (0,len(lista),1):
        soma=soma+((lista[i]-media)**2)
    resultado=(soma/(n-1))**0.5
    return resultado

a=input('Digite o tamanho da lista:  ')
la [ ]

