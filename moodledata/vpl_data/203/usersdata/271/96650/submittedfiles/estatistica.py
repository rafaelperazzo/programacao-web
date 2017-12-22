# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desvio(lista) :
    somatorio = 0
    for i in range(0,len(lista),1) :
        somatorio = somatorio + (lista[i] - media(lista))**2
    desvio = (somatorio/(n-1))**(1/2)
    return desvio

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
#ENTRADA
n = int(input('Digite a quantidade de valores : '))
a = []
b = []
#PROCESSAMENTO
for i in range (0,n,1) :
    valora = float(input('Digite o valor a para lista a : '))
    a.append(valora)
for i in range (0,n,1) :
    valorb = float(input('Digite o valor a para lista b : '))
    b.append(valorb)
#SAIDA
print('%.2f ' % media(a))
print('%.2f ' % desvio(a))
print('%.2f ' % media(b))
print('%.2f ' % desvio(b))



