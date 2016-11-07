# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    d=((1/(n-1))*soma)**0.5
    return d

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a=[]
b=[]
n=int(input('Digite o número de elementos da lista:'))

for i in range(0,n,1):
    a.append(input('Digite os valores de a:'))
    b.append(input('Digite os valores de b:'))
