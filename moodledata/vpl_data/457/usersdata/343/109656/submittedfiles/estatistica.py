# -*- coding: utf-8 -*-
import math

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def variância(lista):
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 