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
    desvio=0
    for i in range(0,len(lista),1):
        desvio=((lista[i] - media)**2)
        return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
x=[]
y=[]
nx=input("digite a quantidade de elemento")
for i in range (0,nx,1):
    x.append(input("digite os elementos"))
xy=input("digite a quantidade de elementos de x ")
for i in range(0,ny,1):
    y.append(input("digite os elementos de y")
