# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.

n=int(input('Informe o número de termos na lista: ')
lista=[]
for i in range(0,len(lista),1):
    lista.append(lista[i])

print(lista)