# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    soma=0
    for i in range(1,len(lista)+1,1):
        soma=soma+((lista[i-1]-media(lista))**2)
    dp=((soma/(len(lista)-1))**0,5)
    return dp
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(int('digite o número de elemetos da lista:'))
l=[]
i=0
while i<n:
    elemento=float(input('digite um número:'))
    l.append(elemento)
    