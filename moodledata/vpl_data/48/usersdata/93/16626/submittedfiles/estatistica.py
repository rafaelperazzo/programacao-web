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
    sd=0
    for i in range(0,len(lista),1):
        sd=sd+(lista[i]-media(lista))**2
    desviop=(sd/(len(lista)-1))**0.5
    return desviop
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('quantidade de elementos: ')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('elementos de 1: '))
for i in range(0,n,1):
    b.append(input('elementos de 2: '))
print('%.2f'%media(a))
print('%.2f'%desvio(a))
print('%.2f'%media(b))
print('%.2f'%desvio(b))
