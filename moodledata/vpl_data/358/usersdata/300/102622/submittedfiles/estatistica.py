# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return print('%.2f' % resultado)

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def dp(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)  
    v = 0
    for i in range(0,len(lista),1):
        v = (cont + (lista[i] - media)**2)/len(lista) 
    d = v**(1/2)
    return print('%.2f' % d)
    
        

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m = int(input('Digite a quantidade de listas: '))
n = int(input('Digite a quantidade de elementos por lista: '))

for i in range(0,m,1):
    lista = []
    for j in range(0,n,1):
        lista.append(int(input('Digite os elementos da lista: ')))
    media(lista)
    dp(lista)
    
    
