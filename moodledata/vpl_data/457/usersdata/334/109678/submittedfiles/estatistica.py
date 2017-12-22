# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio_padrao(lista):
    for i in range(m):
        soma = 0
        for j in range(n):
            soma = soma + ((ma[i][j]-x)**2)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

m = int(input())
n = int(input())

ma = []
for i in range(m):
    lista = []
    for i in range(n):
        lista.append(int(input()))
    ma.append(lista)

for i in range(m):
    x = media(lista[i])