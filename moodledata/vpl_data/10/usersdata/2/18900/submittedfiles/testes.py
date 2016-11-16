# -*- coding: utf-8 -*-
from __future__ import division

'''
1) PASSO 1: Criar a função média
'''

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    
    return (soma/len(a))

'''
2) PASSO 2: 
'''

def somaNumerador(x,y):
    
    mediaX = media(x)
    mediaY = media(y)
    
    soma = 0
    for i in range(0,len(x),1):
        soma = soma + (x[i]-mediaX)*(y[i]-mediaY)
    
    return soma

#SOLUÇÃO 1
def somaDenominador(lista):
    soma = 0
    for i in range (0,len(lista),1):
        soma = soma + (lista[i]-media(lista))**2
    return soma


    
    
    
    
    