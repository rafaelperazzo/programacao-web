# -*- coding: utf-8 -*-

n = int(input('Digite a quantidade de termos da lista: '))
lista1 = []
lista2 = []
for i in range(0,n,1):
    termo=int(input('Digite o valor do termo'+str(i)+' da lista 1: '))
    lista1.append(termo)
    
for i in range(0,n,1):
    termo=int(input('Digite o valor do termo'+str(i)+' da lista 2: '))
    lista2.append(termo)    
    
    
    
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 