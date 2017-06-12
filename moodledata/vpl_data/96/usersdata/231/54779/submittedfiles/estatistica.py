# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def variancia(lista):
    v=0
    for i in range(0,len(lista),1):
        v=v+((lista[i]-media(lista))**2)
    d=(v/len(lista))**0.5
    return d

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a=[1,2,3,4,5]
b=[10,20,30,40,50]
print('%.2f'%media(a))
print(variancia(a))
print(media(b))
print(variancia(b))

