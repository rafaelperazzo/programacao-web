# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def des(lista):
    a=0
    for i in range (0, n, 1):
        a = a+(lista[1]-media(lista))**2
    s = ((1/(n-1))*a)**(0.5)
    return s


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a = []
b = []
n = input("Digite o valor de n:")

for i in range (0, n, 1):
    a.append(input("Digite um elemento A:"))

for i in range (0, n, 1):
    b.append(input("Digite um elemento B:"))

media_a=media(a)
media_b=media(b)
des_a=des(a)
des_b=des(b)

print ("%.2f"%media_a)
print ("%.2f"%des_a)
print ("%.2f"%media_b)
print ("%.2f"%des_b)