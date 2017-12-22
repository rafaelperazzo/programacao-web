# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def dp(lista,n,media):
    cont = 0
    for i in range(0,n,1):
        cont = cont + (a[i] - media)**2
    v = cont/n
    desvio = v**0,5
    return desvio
    
        

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m = int(input('Digite a quantidade de listas: '))
n = int(input('Digite a quantidade de elementos por lista: '))
matriz = []
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input('Digite os elementos da lista: ')))
    matriz.append(linha)
    
 media(matriz)
 dp(matriz,n,media(matriz))