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
    soma=0
    for j in range(0,len(lista),1):
        x=(((lista[j]-media)**2)/(len(lista)-1)**0.5))
        soma = soma + x
        return soma
        



#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 