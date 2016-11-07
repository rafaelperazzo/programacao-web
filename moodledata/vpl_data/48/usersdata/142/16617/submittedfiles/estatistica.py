# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
n=input('Digite um valor n:')
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite um valor:'))

for i in range(0,n,1):
    b.append(input('Digite um valor:'))


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 