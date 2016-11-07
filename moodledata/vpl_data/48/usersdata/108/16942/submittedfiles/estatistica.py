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
        somatorio= somatorio + ((lista[i]-media)**2)
        resultado = somatorio/(n-1)
        return resultado
        
na = input ('Digite o tamanho da lista a:')
a = []

for i in range (0,n,1):
    a.append(input('Digite o elemento:'))
    
nb = input ('Digite o tamanho da lista b:')
b = []

for i in range (0,n,1):
    a.append(input('Digite o elemento:'))
    
        






#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 