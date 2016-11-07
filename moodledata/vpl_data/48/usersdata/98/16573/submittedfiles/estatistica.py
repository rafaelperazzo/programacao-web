# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
 #Definindo a Função do desvio:
 def desvio(lista):
     soma=0
     for i in range(0,len(lista),1):
         soma=soma+(l[i]-(media(lista)))**2
     s=(soma/(len(lista)-1))**0.5
     

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 