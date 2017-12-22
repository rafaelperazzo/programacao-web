# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio (lista):
    somatorio = 0
    for i in range (0,len(lista),1):
        somatorio = somatorio + (lista[i] - media(lista))**2
    desvio = (somatorio / (n-1))**(1/2)
    return (desvio)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 

n = int (input('Digite a quantidade de elementos: '))

a = []
b = []

for i in range (0,n,1):
    valor_a = float(input('Digite o elemento da primeira lista: '))
    valor_b = float(input('Digite o elemento da segunda lista: '))
    a.append (valor_a)
    b.append (valor_b)

print ('%.2f' %media(a))
print ('%.2f' %desvio(a))
print ('%.2f' %media(b))
print ('%.2f' %desvio(b))