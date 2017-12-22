# -*- coding: utf-8 -*-
l=int(input('Digite o número de listas:'))
n=int(input('Digite o número de elementos da lista:'))
lista=[]
for i in range(l):
    lista.append(float(input('Insira elementos:')))
    coluna=[]
    for j in range(n):
        coluna.append(lista)
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
print(lista)

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 