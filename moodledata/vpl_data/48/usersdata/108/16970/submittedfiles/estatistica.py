# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio (lista):
    soma = 0
    for i in range (0,len(lista),1):
        soma = soma + ((lista[i]-media(lista))**2)
    resultado = ((soma/(n-1))**0.5
    return resultado
        
na = input ('Digite o tamanho da lista a:')
a = []

for i in range (0,na,1):
    a.append(input('Digite o elemento:'))
    
nb = input ('Digite o tamanho da lista b:')
b = []

for i in range (0,nb,1):
    b.append(input('Digite o elemento:'))

media_a = media (a)
desvio_a = desvio (a)
media_b = media (b)
desvio_b = desvio (b)

print (media_a)
print (desvio_a)
print (media_b)
print (desvio_b)

    
        






#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 