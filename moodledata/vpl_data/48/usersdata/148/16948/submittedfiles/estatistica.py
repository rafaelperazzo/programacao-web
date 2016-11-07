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
n=input('Digite n:')
a=[]
b=[]
i=0
while i<n:
    a.append(input('Digite um elemento para a lista 1:'))
    i=i+1

i=0
while i<n:
    b.append(input('Digite um elemento para a lista 2:'))
    i=i+1
