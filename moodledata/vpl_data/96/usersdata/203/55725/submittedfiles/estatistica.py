# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def dp(lista):
    soma=0
    for i in range(0,len(lista)-1,1):
        soma = soma + ((l[i]-media)**2)
    resultado=((soma/(n-1))**0.5
    return resultado

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('tamando da lista: '))
