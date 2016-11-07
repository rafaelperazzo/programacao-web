# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
soma=0
def desvio(lista):
    for j in range(0,len(lista),1):
        x=(lista[i]-media(lista))**2
        soma=soma+x
    d=soma**0.5
    return d
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('Digite o número de elementos da lista a:')
m=input('Digite o número de elementos da lista b:')
a=[]
b=[]
for k in range (0,n,1):
    a.append(input('Digite um número para compor a lista a:'))
    b.append(input('Digite um número para compor a lista b:'))
media_a=media(a)
desvio_a=desvio(a)
media_b=media(b)
desvio_b=desvio(b)
print media_a
print desvio_a
print media_b
print desvio_b