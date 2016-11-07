# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desviopadrao(lista):
    soma2=0
    for i in range (0,len(lista),1):
        soma2 = soma2 + ((lista[i] - media(lista))**2) 
    S=(soma2/(len(lista)-1))**0.5
    return S    
