# -*- coding: utf-8 -*-


def media(lista):
    media = sum(lista)/len(lista)
    return media 
    
def desvio_padrao(lista):
    somatorio = 0
    for i in range(0,len(lista),1):
        somatorio = somatorio + ((media(lista) - lista[i])**2)
    desvio = (somatorio/(n - 1))**0.5
    return desvio
   
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
m = int(input('Digite o número de listas: '))
n = int(input('Digite o número de elementos de cada lista: '))
matriz = []
for i in range (0,n,1):

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 