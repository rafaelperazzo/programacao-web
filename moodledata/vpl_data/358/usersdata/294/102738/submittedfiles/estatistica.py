# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio_Padrao(lista):
    soma = 0
    for i in range (0,len(lista),1):
        soma += ((lista[i]-(media(lista))))**2
    p = soma/((len(lista))-1)
    desvio = (p)**(0.5)
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m= int(input('Digite a quantidade de listas: '))
for i in range (0,m,1):
    n= int(input('Digite a quantidade de elementos da lista%d: ' %(i+1)))
    lista=[]
    for i in range(0,n,1):
        lista.append(int(input('Digite o elemento%d da lista: ' %(i+1))))
    print(media(lista))
    print(desvio_Padrao(lista))
    
        