# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('qte de termos:'))
lista1=[]
lista2=[]
for i in range(0,n,1):
    t=float(input('termo:'))
    lista1.append(t)
for i in range(0,n,1):
    t=float(input('termo:'))
    lista2.append(t)    