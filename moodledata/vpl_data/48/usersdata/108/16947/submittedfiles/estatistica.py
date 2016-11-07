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
    resultado = (somatorio/(n-1))**0.5
    return resultado
        
na = input ('Digite o tamanho da lista a:')
a = []

for i in range (0,na,1):
    a.append(input('Digite o elemento:'))
    
nb = input ('Digite o tamanho da lista b:')
b = []

for i in range (0,nb,1):
    a.append(input('Digite o elemento:'))

media_a = media (a)
media_b = media (b)
desviopadrao_a = desviopadrao (a)
desviopadrao_b = desviopadrao (b)

print (media_a)
print (media_b)
print (desviopadrao_a)
print (desviopadrao_b)

    
        






#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 