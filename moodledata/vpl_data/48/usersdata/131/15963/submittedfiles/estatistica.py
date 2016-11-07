# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
a=[]
b=[]
n=input('digite os elementos:')
for i in range (0,n,1):
    a.append(input('digite o valor do elemento:'))
    
for i in range (0,n,1):
    b.append(input('digite o elemento:'))
   
media_a = media(a)
media_b = media(b)
 
print('%.2f:'%media_a)
print('%.2f:'%media_b)
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
