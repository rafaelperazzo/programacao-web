# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(lista):
    desvio=0
    for i in range(0,len(lista),1):
        desvio=((lista[i] - media)**2)
        
    desvio=((desvio)*(1/(n-1)))**(0.5)
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
x=[]
y=[]
n=input('digite o número de elementos:')

for i in range(0,n,1):
    x.append(input('digite um elemento:')
for i in range(0,n,1):
    y.append(input('digite um elemento:')

