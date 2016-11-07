# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-media(lista)**2)
    resultado=(soma/n-1)**0.5
    return resultado
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a=[]
b=[]
n=input(' digite a quantidade de elementos:')
for i in range(0,n,1):
    a.append(input('digite um elemento:')
for i in range(0,n,1):
    b.append(input('digite um elemento:')

media_a=media(a)
media_b=media(b)
desviopadrao_a=desviopadrao(a)
desbiopadrao_b=desviopadrao(b)
#saida
print media_a
print media_b
print desviopadrao_a
print desviopadrao_b