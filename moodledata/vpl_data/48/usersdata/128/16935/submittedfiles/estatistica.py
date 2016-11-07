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
    for i in range (0,len(lista),1):
        somatorio=somatorio+((lista[i]-resultado)**2)
        dp=((1/(n-1))*somatorio)**0.5
        return dp
    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 