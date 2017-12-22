# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    for i in range (0,len(lista),1):
        lista[i] = ((lista[i] - media(lista))**2)
    dp = (((sum(lista))/(len(lista) - 1))**(0.5))
    return dp 
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m = int(input('informe a quantidade de listas: '))
n = int(input('informe a quantidade de elementos na lista: '))


matriz = []
for i in range (0,m,1):
linhas = []
    for j in range (0,n,1):
        linhas.append(float(input('informe os elementos da lista: ')))
    matriz.append(linhas)

for i in range (m):
    print(media(matriz[i]))

for i in range (m):
    print(desvio(matriz[i]))


    

