# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def desvio(lista):
    soma = 0
    for i in range (0, len(lista), 1):
        soma = soma + ((lista[i]-media(lista))**2)
        s = (soma/(n-1))**(0.5)
        return s
    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

a = []
b = []
n = input('Digite a quantidade de elementos: ')

for i in range (0,n,1):
    a.append(input('Digit o elemento da lista: '))
for i in range (0,n,1):
    b.append(input('Digit o elemento da lista: '))
    
media_a = media(a)
media_b = media(b)
desvio_a = desvio(a)
desvio_b = desvio(b)

print ('%.2f' %media_a)
print ('%.2f' %media_b)
print ('%.2f' %desvio_a)
print ('%.2f' %desvio_b)