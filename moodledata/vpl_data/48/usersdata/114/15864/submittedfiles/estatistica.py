# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviop(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista(i) - media)**2)
    desviop= (soma/(n-1))**0.5
    return desviop


    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 