# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
def desvio(lista):
    soma2 = 0
    for j in range(0,len(lista),1):
        soma2 = (soma2 + ((lista[j] - media(lista))**2))/(len(lista) -1)
        resultado = soma2**0.5
        return resultado

n = input('Digite o número de elementos:')
a = []
b = []

for i in range(0,n,1):
    a.append(input('digite o valor do elemento:'))

for j in range(0,n,1):
    b.append(input('digite o valor do elemento:'))

print('%.2f' %media(a))
print('%.2f' %desvio(a))
print('%.2f' %media(b))
print('%.2f' %desvio(a))
