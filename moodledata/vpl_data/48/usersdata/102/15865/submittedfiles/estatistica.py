# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
a=[]
b=[]
n=input('digite a quantidade de elementos :')


for i in range(0,n,1):
    a.append(input('digite um elemento '))
soma=0
for i in range (0,n,1):
    b.append(input('digite um elemnto '))
    
media_a=media(a)
media_b=media(b)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 