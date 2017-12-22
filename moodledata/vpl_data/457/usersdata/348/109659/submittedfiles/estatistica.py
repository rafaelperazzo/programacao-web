# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista







#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m = int(input('informe a quantidade de listas: '))
n = int(input('informe a quantidade de elementos na lista: '))


matriz = []
for i in range (1,m,1):
linhas = []
    for j in range (1,n,1):
        linhas.append(float(input('informe os elementos da lista: ')))
    matriz.append(linhas)
    


    

