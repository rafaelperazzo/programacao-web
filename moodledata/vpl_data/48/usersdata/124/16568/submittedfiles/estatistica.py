# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def dp(lista):
    b = 0
    s = 0
    for i in range(0, len(lista), 1):
        s = s + lista[i]
    m = s/len(lista)
    for i in range(0, len(lista), 1):
        b = b + (lista[i] - m)**2
    dp = (b/(n-1))**(1/2)
    return dp
    
n = input('Digite o número de valores da lista: ')
a = []
c = []
for i in range (0, n, 1):
    a.append(input('Digite um valor para a lista de a: '))
for i in range(0, n, 1):
    c.append(input('Digite o valor para a lista de c: '))
media_a = media(a)
media_c = media(c)
dp_a = dp(a)
dp_c = dp(c)
print ('%.2f' %media(a))
print ('%.2f' %media(c))
print ('%.2f' %dp(a))
print ('%.2f' %dp(c))
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 