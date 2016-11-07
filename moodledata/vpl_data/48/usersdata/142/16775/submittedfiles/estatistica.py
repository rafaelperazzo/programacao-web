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
    somatorio = 0
    for i in range (0,len(lista),1):
        somatorio = somatorio + ((lista[i]-media)**2)
    dp = (somatorio/(n-1))**0.5
    return dp


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('Digite um valor n:')
a = []
b = []

for i in range(0,n,1):
    a.append(input('Digite um valor:'))

for i in range(0,n,1):
    b.append(input('Digite um valor:'))

media_a = media(a)
desvio_a = desvio(a)
media_b = media(b)
desvio_b = desvio(b)

print ('%.2f'%media_a)
print ('%.2f'%desvio_a)
print ('%.2f'%media_b)
print ('%.2f'%desvio_b)