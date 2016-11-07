# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desviopadrao (lista):
    somatorio=0
    for i in range (0,len(lista),1):
        somatorio= somatorio + ((lista[i]-media)**2/(n-1))
        return somatorio
        
n = input ('Digite o tamanho da lista:')
for i in range (0,n,1):
    lista.adeppend
        






#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 