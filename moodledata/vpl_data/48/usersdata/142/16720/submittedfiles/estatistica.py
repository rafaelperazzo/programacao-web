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
    for i in range (0,n,1):
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

mediaA = media(a)
desvioA = dp(a)
mediaB = media(b)
desvioB = dp(b)

print ('%.2f'%mediaA)
print ('%.2f'%desvioA)
print ('%.2f'%mediaB)
print ('%.2f'%desvioB)