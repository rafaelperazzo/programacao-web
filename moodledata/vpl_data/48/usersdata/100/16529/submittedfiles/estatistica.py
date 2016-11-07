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
    soma1= 0
    for i in range (0,n,1):
        x = (lista - resultado)**2
        soma1=soma1 +x
        
    z = (resultado/(n-1))**(1/2)
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
print resultado