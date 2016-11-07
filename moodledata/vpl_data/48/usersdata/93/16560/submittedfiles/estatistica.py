# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
sd=0
def desvio(lista):
    for i in range(0,len(lista),1):
        sd=sd+(lista[i]-media(lista))**2
    print(sb)
    desvio=(sd/(len(lista)-1))**0.5
    return desvio
a=[0,0,0,0,0,0,0,0,0,0]
b=desvio(a)
print(b)
 

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 