# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dp(lista):
    soma1= 0
    for j in range (0,len(lista),1):
        x = (lista[j] - media(lista))**2
        soma1=soma1 +x
    z = (media(lista) /(n-1))**(1/2)
    return dp
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n = input ('Digite a quantidade de elementos das listas:')
a = [] 
b = []
for k in range (0,n,1):
    a.append(input ('Digite os elementos da lista A:'))
for l in range (0,n,1):
    b.append(input ('Digite os elementos da lista B:'))
print ('%.2f'%media(a))
print (dp(a))
print ('%.2f'%media(b))
print (dp(b))