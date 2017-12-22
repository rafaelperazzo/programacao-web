# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def var(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio=somatorio+(lista[i]-media)**2
    delta=(1/(n-1))*somatorio
    var=delta**(1/2)
    return(var)
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 